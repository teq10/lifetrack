__author__ = 'tangenqing'
# -*- coding: utf-8 -*-

import sys
import xml.etree.ElementTree as ET
from hashlib import sha1
from base import *
from setting import settings
from util.log import logger
from content import content_ope


class WeixinHandler(BaseHandler):
    def check_xsrf_cookie(self):
        return True
    ##verify
    def get_default(self):

        echostr = self.get_argument('echostr', '')
        if echostr and self.verification():
            self.write(echostr)
            res = "weixin callback success"
        else:
            self.write("")
            res = "weixin callback failed"
        log_info = {"handler": __name__ + '.' + self.__class__.__name__, "event": sys._getframe().f_code.co_name,
                    "event_description": "", "res_type": "xml", "res_content": {"message": res, "echostr": echostr}}
        logger.info(log_info)

    def verification(self):

        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')

        token = settings.get("token")

        tmplist = [token, timestamp, nonce]
        tmplist.sort()
        tmpstr = ''.join(tmplist)
        hashstr = sha1(tmpstr).hexdigest()

        if hashstr == signature:
            logger.info("connect with weixin server success!")
            return True
        logger.warn("connect with weixin server fail!")
        return False

    def post_default(self):
        msg = self.get_msg()
        # print msg
        try:
            msg_type = msg['MsgType']
            if self.verification():
                #add cookie
                self.set_secure_cookie("openid", msg["FromUserName"])

                info = getattr(self, 'post_' + msg_type)(msg)
            else:
                info = u"Message verification failed"
            if info:
                logger.info("send a message to weixin, info = " + info)
                self.write(self.rep_text(msg, info))
            else:
                self.write(self.rep_text(msg, u"不好意思，没处理好你的信息，请联系我的主人~"))
        except Exception, e:
            logger.error(e)

    def get_msg(self):
        return self.parse_msg(self.request.body)

    def parse_msg(self, rawmsgstr):
        root = ET.fromstring(rawmsgstr)
        msg = {}
        for child in root:
            msg[child.tag] = child.text
        return msg

    # 事件处理
    def post_event(self, msg):
        event = msg['Event']
        return getattr(self, 'event_' + event)(msg)

    def event_subscribe(self, msg):
        openid = msg["FromUserName"]
        logger.info("event_subscribe: a new user openid =  " + str(openid))
        return self.rep_follow(msg)

    def event_unsubscribe(self, msg):

        openid = msg["FromUserName"]
        logger.info("event_unsubscribe: user openid =  " + str(openid))
        return self.rep_unfollow(msg)

    def event_CLICK(self, msg):
        msg['Content'] = msg['EventKey']
        return '这是一个点击'

    def event_VIEW(self, msg):
        return '这是一个视频'



    #文本处理
    def post_text(self, msg):
        try:
            openid = msg['FromUserName']
            keyword = msg['Content'].strip().encode('utf-8')
            logger.info("get text: user openid =  " + str(openid) + ";msg = " + keyword)

            if not keyword.startswith("hi"):
                info = "每日记录要以hi开头，我才记录哦"
            else:
                today = self.curr_date
                month = self.curr_month
                info = content_ope.record_msg(openid, keyword[2:], month, today)
            return info
        except Exception, e:
            logger.error(e)
            return "不好意思，发生了一点错误，请联系我的主人"

    def post_image(self, msg):  #图片消息
        try:

            openid = msg['FromUserName']
            url = msg['PicUrl']
            logger.info("get a photo: user openid =  " + str(openid) + ";photo = " + url)

            today = self.curr_date
            month = self.curr_month
            info = content_ope.record_photo(openid, url, month, today)
            return info
        except Exception, e:
            logger.error(e)
            return "不好意思，发生了一点错误，请联系我的主人"
    def post_voice(self, msg):  #
        return "这是一段声音" + "我还不能处理"

    def post_video(self, msg):
        return "这是一段视频" + "我还不能处理"

    def post_location(self, msg):
        return "这是一个地址" + "我还不能处理"

    def post_link(self, msg):
        return "这是一个链接" + "我还不能处理"

    def post_shortvideo(self, msg):
        return "这是一段短视频" + "我还不能处理"



    #回复消息

    def rep_text(self, msg, text):
        rep_info = """
                    <xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    </xml>
                    """
        info = rep_info % (msg['FromUserName'], msg['ToUserName'],
                           str(int(time.time())), str(text))

        return info

    def rep_default(self, msg):
        return '我暂时还不支持接收这种消息'

    def rep_follow(self, msg):
        return 'hello~欢迎关注"一张图一句话"！在这里你可以每天发一张图，一句话，不可修改！<br/> ' \
               '平淡的日子太多，精彩的瞬间让我来帮你记录~<br/>' \
               '让我们认真工作，放肆生活^_^'

    def rep_unfollow(self, msg):
        return 'byebye'




    def gen_timetoken(self, weixinid):
        now = str(time.strftime('%Y%m%d%H', time.localtime(time.time())))
        minite = str(time.localtime(time.time()).tm_min / 10)
        timetoken = ''.join([weixinid, now, minite])
        return sha1(timetoken).hexdigest()

__author__ = 'tangenqing'
# -*- coding: utf-8 -*-

from util.fileope import file_ope
from setting import contents
from setting import settings
import os

class Content(object):
    CONTENT = "content"
    MONTH = "month"
    MSG = "msg"
    PHOTO = "photo"
    def record_msg(self, openid, msg, month, today):
        if self.refresh_data(openid, month):
            key = today + "_" + self.MSG
            if key in contents[openid][self.CONTENT]:
                info = "今日文字已经记录了哦，不可变更"
            else :
                path = os.path.join(settings['data_path'], openid, month)
                file_ope.append_data(path, key + "," + msg)
                contents[openid][self.CONTENT][key] = msg
                info = today + ": 今日文字记录已经帮你记录好了！"
        else:
            info = "发生了错误，请联系我的主人"
        return info

    def record_photo(self, openid, url, month, today):
        if self.refresh_data(openid, month):
            key = today + "_" + self.PHOTO
            if key in contents[openid][self.CONTENT]:
                info = "今日图片已经记录了哦，不可变更"
            else :
                path = os.path.join(settings['data_path'], openid, month)
                file_ope.append_data(path, key + "," + url)
                contents[openid][self.CONTENT][key] = url
                info = today + ": 今日图片记录已经帮你记录好了！"
        else:
            info = "发生了错误，请联系我的主人"
        return info

    def refresh_data(self, openid, month):
        if openid in contents and month == contents.get(openid).get(self.MONTH):
            return True

        path = os.path.join(settings['data_path'], openid, month)
        content = file_ope.parse_data(path)
        if content is None:
            return False
        else:
            contents[openid] = {self.MONTH: month, self.CONTENT: file_ope.parse_data(path)}
            return True
content_ope = Content()

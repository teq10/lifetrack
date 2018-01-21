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
                root_path = os.path.join(settings['data_path'], openid)
                real_path = os.path.join(openid, month + "_pics",
                                         file_ope.download_and_save(url, os.path.join(root_path, month+"_pics")))
                file_ope.append_data(os.path.join(root_path, month), key + "," + real_path)
                contents[openid][self.CONTENT][key] = real_path
                info = today + ": 今日图片记录已经帮你记录好了！"
        else:
            info = "发生了错误，请联系我的主人"
        return info

    def refresh_data(self, openid, month):
        if openid in contents and month == contents.get(openid).get(self.MONTH):
            return True
        path_dir = os.path.join(settings['data_path'], openid)
        file_ope.create_path(path_dir)
        file_ope.create_path(os.path.join(path_dir, month+"_pics"))
        path_file = os.path.join(path_dir, month)
        content = file_ope.parse_data(path_file)
        if content is None:
            return False
        else:
            contents[openid] = {self.MONTH: month, self.CONTENT: content}
            return True
content_ope = Content()
if __name__ == "__main__":
    # logger.init(logpath="log/", log_level="DEBUG")

    print content_ope.record_photo("eqwe","eewtqwe","2018-01", "2018-01-02")
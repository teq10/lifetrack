# -*- coding: utf-8 -*-
import random
import string

__author__ = 'tangenqing'

import urllib
import os
from log import logger


class Fileope(object):

    def is_exit(self, path):
        return os.path.exists(path)

    def create_path(self, path):
        if not self.is_exit(path):
            os.makedirs(path)
            logger.info(path + ": dir create success!")
        else:
            logger.info(path + ": dir already exists! ")

    def create_file(self, path):
        if not self.is_exit(path):
            os.system("touch " + path)
            logger.info(path + ": file create success!")
        else:
            logger.info(path + ": file already exists!")

    def append_data(self, path, data):
        fp = open(path, 'a')

        try:
            fp.writelines(data + ",\n")
            return True

        except Exception,e:
            logger.error("write to file fail: " + data + e)
            return False
        finally:
            fp.close()

    def parse_data_list(self, path):
        if not self.is_exit(path):
            logger.warn(path + ": file data not exist")
            return []
        fp = open(path, 'r')
        try:

            value = {}
            for line in fp:
                kw = line.split(',')
                kkw = kw[0].split('_')
                if kkw[0] in value:
                    value[kkw[0]][kkw[1]] = kw[1]
                else:
                    value[kkw[0]] = {"date": kkw[0], kkw[1]: kw[1]}

            return dict2list(value)
        except Exception, e:
            logger.error(path + " read file fail: " + e)
            return None
        finally:
            fp.close()


    def parse_data(self, path):
        if not self.is_exit(path):
            self.create_file(path)
            logger.warn(path + ": file data not exist")
            return {}
        fp = open(path, 'r')
        try:

            value = {}
            for line in fp:
                kw = line.split(',')
                value[kw[0]] = kw[1]
            return value
        except Exception, e:
            logger.error(path + " read file fail: " + e)
            return None
        finally:
            fp.close()

    def download_and_save(self, url, path):
        try:
            if not self.is_exit(path):
                    logger.info('文件夹' + path + '不存在，重新建立')
                    self.create_path(path)

            file_name = ''.join(random.sample(string.ascii_letters + string.digits, 8))+".jpg"
            #拼接图片名（包含路径）
            filename = os.path.join(path, file_name)
            #下载图片，并保存到文件夹中
            urllib.urlretrieve(url, filename=filename)
            return file_name
        except IOError as e:
                logger.error('file ope error' + str(e))
        except Exception as e:
                logger.error('error ：'+ str(e))



def dict2list(value):
    keys=value.keys()
    keys.sort(reverse=True)
    results=[value[key] for key in keys]
    return results
logger.init(logpath="log/", log_level="DEBUG")
file_ope = Fileope()

if __name__ == "__main__":
    logger.init(logpath="log/", log_level="DEBUG")
    path = "/Users/tangenqing/Documents/git/python/lifetrack/data/eqwe"
    tt = Fileope()

    print os.path.join("dd", "2dddd" + "_pics", tt.download_and_save("http://mmbiz.qpic.cn/mmbiz_jpg/w8ZWQibfjlADfUvh5NF0zMMTnG9NrYwBykWNTbfw8pKIaLWUX9IzFcdD8wic9Ooo4gMibTjTAox308PzydJPTu4FA/0",path))
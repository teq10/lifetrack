__author__ = 'tangenqing'
# -*- coding: utf-8 -*-
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

def dict2list(value):
    keys=value.keys()
    keys.sort(reverse=True)
    results=[value[key] for key in keys]
    return results
logger.init(logpath="log/", log_level="DEBUG")
file_ope = Fileope()

if __name__ == "__main__":
    logger.init(logpath="log/", log_level="DEBUG")
    path = "/Users/tangenqing/Documents/git/python/lifetrack/data/eqwe/2018-01"
    tt = Fileope()
    print tt.parse_data_list(path)
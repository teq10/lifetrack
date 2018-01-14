# -*- coding: utf-8 -*-
"""
该日志类可以把不同级别的日志输出到不同的日志文件中
"""

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


class Log(object):
    LOG_LEVELS = {"DEBUG": 10, "INFO": 20, "WARN": 30, "ERROR": 40}

    def init(self, logname='lifetrack',
             logpath='/tmp/',
             log_level='INFO',
             log_format='%(message)s',
             log_backcount=0,
             log_filesize=10 * 1024 * 1024):

        self.__loggers = {}
        self.logname = logname
        self.log_format = log_format
        self.log_backcount = log_backcount
        self.log_filesize = log_filesize

        self.log_path = {
            'debug': os.path.join(logpath, 'debug/' + logname + '.debug.log'),
            'info': os.path.join(logpath, 'info/' + logname + '.info.log'),
            'warn': os.path.join(logpath, 'warn/' + logname + '.warn.log'),
            'error': os.path.join(logpath, 'error/' + logname + '.error.log')
        }

        log_levels = self.log_path.keys()

        self.create_handlers()

        for level in log_levels:
            logger = logging.getLogger(self.logname + '.' + level)
            logger.addHandler(self.handlers[level])
            logger.setLevel(self.LOG_LEVELS[log_level])
            self.__loggers.update({level: logger})

    def get_log_message(self, level, message):
        # frame,filename,lineNo,functionName,code,unknowField = inspect.stack()[2]
        """日志格式：[时间] [类型] [记录代码] 信息"""
        if type(message) != dict:

            message = dict(message=message)

        message.update({"req_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')})
        message.update({"level": level})

        return self.log_format % dict(message=message)

    def create_handlers(self):

        self.handlers = {}

        logLevels = self.log_path.keys()

        for level in logLevels:
            path = os.path.abspath(self.log_path[level])

            # 日志存储路径，不存在，就创建该路径
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))

            self.handlers[level] = TimedRotatingFileHandler(path, 'H', 1, backupCount=self.log_backcount)

            formatter = logging.Formatter(self.log_format)

            self.handlers[level].setFormatter(formatter)
            self.handlers[level].suffix = "%Y%m%d%H.log"

    def info(self, message):
        message = self.get_log_message("info", message)
        self.__loggers['info'].info(message, exc_info=0)

    def error(self, message):
        message = self.get_log_message("error", message)
        self.__loggers['error'].error(message, exc_info=1)

    def warn(self, message):
        self.__loggers['warn'].warning(message, exc_info=0)

    def debug(self, message):
        message = self.get_log_message("debug", message)
        self.__loggers['debug'].debug(message, exc_info=0)


logger = Log()
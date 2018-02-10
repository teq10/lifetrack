__author__ = 'tangenqing'
# -*- coding: utf-8 -*-

import os
from base import *
from util.log import logger
from util.fileope import file_ope
from setting import settings


class TrackHandler(BaseHandler):
    def get_default(self):
        id = self.get_argument('id', '')
        month = self.get_argument('month', self.curr_month)
        path = os.path.join(settings['data_path'], id, month)
        content = file_ope.parse_data_list(path)
        logger.info("get track data, openid="+ id + ",month=%s" +  month)
        self.render("index.html", content=content, month= month)

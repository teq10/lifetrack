# -*- coding: utf-8 -*-

import os
import datetime,time

from tornado.options import define, options

define("port", default=80, help="run on the given port", type=int)
define("logpath", default="log/", help="log path")


settings = {}

settings['debug'] = True
settings['root_path'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "")
settings['template_path'] = os.path.join(settings['root_path'], "template")
settings['static_path'] = os.path.join(settings['root_path'], "data")
settings['token'] = "0cf21ca674ee11e3987122000afa135c"
settings['data_path'] = os.path.join(settings['root_path'], "data")
settings['wx3124892de8d1e667'] = {'access_token': "",'expires_in': 0, 'create_time': 0}


settings['xsrf_cookies'] = False
settings['cookie_secret'] = "EEB1C2AB05DDF04D35BADFDF776DD4B0"
settings['log_level'] = "DEBUG"

contents = {}

if __name__ == "__main__":
    path = os.path.join(settings['data_path'], "1", "test")
    print os.path.exists(path)



import os
from tornado.options import define, options

define("port", default=80, help="run on the given port", type=int)
define("logpath", default="log/", help="log path")


settings = {}

settings['debug'] = True
settings['root_path'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "")
settings['template_path'] = os.path.join(settings['root_path'], "template")
settings['static_path'] = os.path.join(settings['root_path'], "static")

settings['wx3124892de8d1e667'] = {'access_token': "",'expires_in': 0, 'create_time': 0}


settings['xsrf_cookies'] = False
settings['cookie_secret'] = "EEB1C2AB05DDF04D35BADFDF776DD4B0"
settings['log_level'] = "DEBUG"

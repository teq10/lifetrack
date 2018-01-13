# -*- coding: utf-8 -*-

# 旅游服务地址

URL_TOUR = "www.ssp-travel.com"
URL_MAIN = "http://" + URL_TOUR + "/Smart_Service_Platform/SearchResultOnly_WeiXin.jsp?SearService=%s"
URL_WEB = "http://" + URL_TOUR + "/Smart_Service_Platform/SearchResultOnly_WeiXinWeb.jsp?SearService=%s"
URL_HOTEL = "http://" + URL_TOUR + "/Smart_Service_Platform/Weixin_Hotel.jsp"
URL_SPOT = "http://" + URL_TOUR + "/Smart_Service_Platform/Weixin_Spot.jsp"
URL_RESTAURANT = "http://" + URL_TOUR + "/Smart_Service_Platform/Weixin_Restaurant.jsp"

#百度地图显示路线
URL_ROUTE = "http://" + URL_TOUR + "/Smart_Service_Platform/showherf.jsp?length="
URL_SERVICE = "http://" + URL_TOUR + "/Smart_Service_Platform/Weixin_%s.jsp"

# 微信公众号

WXAPP = "wx3124892de8d1e667"
WXAPP_SECRET = "e83f890a44dde1278bb7b4f038f81e29"
TOKEN = "0cf21ca674ee11e3987122000afa135c"
ENCODE_KEY = "AH1dAUpj7g05OMq9qdbgeLwUEdvYQ7ugQHbA0zl2bF0"


# 微信api常量定义
WXAPI_AUTHORIZE = "https://open.weixin.qq.com/connect/oauth2/authorize?appid={APPID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={SCOPE}&state={STATE}#wechat_redirect"
WXAPI_WXUSER_ACCESS_TOKEN = "https://api.weixin.qq.com/sns/oauth2/access_token?appid={APPID}&secret={SECRET}&code={CODE}&grant_type=authorization_code"
WXAPI_USERINFO = "https://api.weixin.qq.com/sns/userinfo?access_token={ACCESS_TOKEN}&openid={OPENID}&lang=zh_CN"

WXAPI_SUBSCRIBED_USERINFO = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN"

#token and  menu

URL_ACCESS_TOKEN = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"
URL_GET_MENU = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s"
URL_CREATE_MENU = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s"
URL_DEL_MENU = ""


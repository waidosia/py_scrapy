#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 常量定义
Desc : 
"""
from tender.utils import const

# 检索关键字配置文件
const.KEYWORD_CONF = 'keyword.conf'
# 网站名称关键字
const.WEBNAME_CONF = 'webname.conf'

# pymongo参数
const.MONGO_URI = '127.0.0.1'
const.MONGO_DATABASE = 'tender'
const.MONGODB_PORT = '27017'

# email收件人组
const.EMAIL_CONF = ['xxx',]

# 第三方 SMTP 服务
const.MAIL_HOST = "xxx"  # 设置服务器
# 发送者Email地址
const.SENDER = 'xxx'
# 发送者Email密码,之前是密码，现在是口令
const.MAIL_PASS = "xxx"  # 口令

# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/little-flower/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": False,
    "repo": "william-han-wang/little-flower@gh-pages"
}

# 站点设置
site_name = "汉伊斯特鲁伊的风与影"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "汉"
email = "uniwanghan@gmail.com"
author_homepage = "https://sites.google.com/site/woshihanwang/"
description = "Skywalker in the air"
key_words = ['blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/uniwanghan",
        "icon": "gi gi-twitter"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''

valine = {
    "enable": True,
    "appId": "Uey4o08sIktXtBQHe9h62BlP-gzGzoHsz",
    "appKey": "cJmWOSNH5jXyGrQMBCmTHCNt",
    "notify": "false",
    "visitor": "false",
    "recordIP": "false",
    "serverURLs": None,
    "placeholder": "Just comment~"
}

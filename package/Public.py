# -*- coding: UTF-8 -*-
import os
import time

# mode = Return Style
from Method import BaiduWenKu


def GetTime(mode):
    NA = time.time()
    match mode:
        case 0:  # Native Time
            return NA
        case 1:  # Native Local Time
            return time.localtime(NA)
        case 2:
            return time.strftime("%Y-%m-%d | %H:%M:%S")
        case 3:
            return time.strftime("%Y %a %b %d | %H:%M:%S")
        case 4:
            return "N/A"


def AnalyzeURL(url):
    if url.startswith('https://max.book118.com/'):
        print('检测到为 原创力 链接')
        return 0
    elif url.startswith('https://xuanshu.hep.com.cn/'):
        print('检测到为 高等教育出版社产品信息检索系统 链接')
        return 1
    elif url.startswith('https://wenku.baidu.com/'):
        print('检测到为 百度文库 链接')
        return 2
    elif url.startswith('9998'):
        return 9998
    elif url.startswith('9999'):
        return 9999


def CookiesInfo():
    list = []
    try:
        if BaiduWenKu.ReadCookies() is not None:
            list.append('百度')
    except:
        print('百度 Cookies 读取失败')

    print("当前 保存的 Cookies 有:", list)
    pass


def MakeBaseDir(dirs):
    for Dir in dirs:
        try:
            os.mkdir('.\\' + Dir)
        except:
            pass


def StartInfo():
    print(
        """
####################################
        FreeDoc Download
####################################

___________________________________
-目前支持: 
    -原创力免费预览部分
    -高等教育出版社产品信息检索系统样章部分
    -百度文库(Word文档) 
    Tips: 如果下载不全请确认去除链接?后面的东西，如果依然不行请重新获取Cookies
-当前时间: %s
-你可以直接输入链接来自动下载
____________________________________
-输入 9999 来 查看该软件保存的 Cookies
-输入 9998 来 保存一些网站所需要的 Cookies

"""
        % GetTime(2)
    )

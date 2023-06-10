# -*- coding: UTF-8 -*-
import os

# mode = Return Style
from Method import BaiduWenKu


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
    elif url.startswith('https://www.docin.com/'):
        print('检测到为 豆丁网 链接')
        return 3
    elif url.startswith('9998'):
        return 9998
    elif url.startswith('9999'):
        return 9999


def CookiesInfo():
    _list = []
    try:
        if BaiduWenKu.ReadCookies() is not None:
            _list.append('百度')
    except IOError:
        print('百度 Cookies 读取失败')

    print("当前 保存的 Cookies 有:", _list)
    pass


def MakeBaseDir(dirs):
    for Dir in dirs:
        try:
            os.mkdir('.\\' + Dir)
        except IOError:
            pass


def StartInfo():
    print(
        """
####################################
        FreeDoc Download
####################################
     你可以直接输入链接来自动下载
___________________________________
-目前支持: 
    -原创力免费预览部分
    -高等教育出版社产品信息检索系统样章部分
    -百度文库(Word文档) 
     -Tips: 如果下载不全请确认去除链接?后面的东西，如果依然不行请重新获取Cookies
    -豆丁网
     -Tips: 利用图片合成pdf的方法(有水印)
____________________________________
-输入 9999 来 查看该软件保存的 Cookies
-输入 9998 来 保存一些网站所需要的 Cookies
"""
    )

# -*- coding: UTF-8 -*-
import time


# mode = Return Style
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



def StartInfo():
    print(
        """
📕FreeDoc Download
🎯目前支持: 原创力免费预览部分,高等教育出版社产品信息检索系统样章部分
🕙当前时间: %s
----------------------------------
"""
        % GetTime(2)
    )

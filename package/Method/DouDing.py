import re

from bs4 import BeautifulSoup

import API.Request

def Dump(url):
    pid = str(url).split('-')[1].split('.')[0]
    native = BeautifulSoup(API.Request.RequestWebSite('https://www.docin.com/p-3711178666.html'), "lxml")
    pats = re.compile('flash_param_hzq:"(.+)"')
    tats = re.compile('title:"(.+)"')
    pata = re.compile('allPage:(.+),')
    sid = pats.search(str(native)).group(0).split('"')[1]
    title = tats.search(str(native)).group(0).split('"')[1]
    page = pata.search(str(native)).group(0).split(':')[1].split(',')[0]
    return pid, sid, page, title
    pass


def Method1(pid, sid, page):
    plist = []
    for pg in range(1, int(page)+1):
        plist.append(
                f'http://221.122.117.73/docinpic.jsp?sid={sid}&file={pid}&width=9999&pageno={pg}'
        )
    return plist
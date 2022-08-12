import re

from bs4 import BeautifulSoup

import API.Request


def Dump(html):
    Native = BeautifulSoup(html, "lxml")
    # print(Native)
    title = Native.title.string
    print('文件标题为: ', title)
    PageURL = ''
    items = Native.find_all('a', href=True)
    for a in items:
        if a['href'].startswith('/front/book/previewBookResource'):
            PageURL = a['href']
    PageURL2 = 'https://xuanshu.hep.com.cn/' + PageURL
    print('样章预览链接为: ', PageURL2)

    Native2 = BeautifulSoup(API.Request.RequestWebSite(PageURL2), "lxml")
    # Get After
    a1 = re.compile(r"window.defaultPdfUrl = (.*?)$", re.S)
    # print(a1)
    a = Native2.find('script', text=a1)
    # print(a)
    PageURL3 = a1.search(a.text).group(1).split(';')[0].split("'")[1]
    print('真实PDF链接为: ', PageURL3)

    return title, PageURL3
    pass

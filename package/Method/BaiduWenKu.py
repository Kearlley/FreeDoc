import json
import re
from time import sleep

from bs4 import BeautifulSoup
from docx import Document
from selenium import webdriver
from selenium.webdriver.common.by import By

from API import Request
from API.Public import GetWorkPath

option = webdriver.EdgeOptions()
option.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

Cookies = {}


def SaveCookies(username, password):
    # driver = None
    print(option.binary_location)
    print('将自动打开浏览器自动完成操作(可能需要手动过人机验证)')
    path = GetWorkPath() + r'\driver\msedgedriver.exe'
    print(path)
    driver = webdriver.Edge(path)

    # driver = webdriver.Firefox('.\\driver\\geckodriver.exe')
    # driver = webdriver.Chrome('.\\driver\\chromedriver.exe')

    driver.get('https://wenku.baidu.com/')
    sleep(1)  # Wait WebSite
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/div[2]/a').click()
    sleep(3)  # Waite WebSite
    driver.find_element(by=By.XPATH, value='//*[@id="TANGRAM__PSP_11__userName"]').send_keys(username)
    driver.find_element(by=By.XPATH, value='//*[@id="TANGRAM__PSP_11__password"]').send_keys(password)
    driver.find_element(by=By.XPATH, value='//*[@id="TANGRAM__PSP_11__submit"]').click()

    print('程序将在 60 秒后获取Cookies，请在 60 秒内完成剩余验证操作')
    sleep(60)  # Wait Login End

    dictCookies = driver.get_cookies()
    Cookies[dictCookies[2]['name']] = dictCookies[2]['value']  # Token
    Cookies[dictCookies[5]['name']] = dictCookies[5]['value']  # ID
    # print(Cookies)
    print('Cookies 获取成功')
    with open('.\\cookies\\baidu.cks', 'w+') as file:
        try:
            file.write(str(Cookies))
            print("Cookies 写入成功")
        except:
            print("File Write Err")
    driver.close()


def ReadCookies():
    with open('.\\cookies\\baidu.cks', 'r+') as baidu:
        a = eval(baidu.read())
        print(type(a))
        return a
    pass


def Dump(html):
    print('开始数据分析...')
    Native = BeautifulSoup(html, "lxml")
    a1 = re.compile(r"pageData = (.*?);$", re.MULTILINE)  # index pageData
    a = Native.find('script', text=a1)
    PageData = a1.search(a.text).group(1)  # Get
    JPageData = json.loads(PageData)

    # Get Data
    Title = JPageData['viewBiz']['docInfo']['title']
    Page = JPageData['viewBiz']['docInfo']['page']
    FileType = JPageData['viewBiz']['docInfo']['fileType']
    # PageHeight = JPageData['readerInfo']['pageInfo']['pageHeight']
    # pageWidth = JPageData['readerInfo']['pageInfo']['pageWidth']
    PageIndex = JPageData['readerInfo']['htmlUrls']['json']

    return Title, Page, FileType, PageIndex
    pass


def GetPageIndexUrl(lists):
    __list = []
    __page = []
    for _list in lists:
        __list.append(_list['pageLoadUrl'])
        __page.append(_list['pageIndex'])
    return __list, __page
    pass


pattern = re.compile('{\'.*?}')


def Doc_RePage(urls, title):  # FOr num +
    document = Document()
    # document.styles['Normal'].font.size = Pt(5)
    num = 0
    for url in urls:
        print(url)
        num += 1
        # print(num)
        response = Request.RequestWebSite(url)
        #print(response)
        response2 = response.split('wenku_' + str(num) + '(')[1].split(')')[0]  # wenku_1(.*？)
        response_body = json.loads(response2)['body']
        # print(response_body)
        for c in response_body:
            # print(num)
            # c1 = json.loads(c)
            # print(c)
            cw = c['c']
            p1 = re.sub(pattern, '', str(cw))  # Cut {'*}
            # p = re.search(pattern,str(cw))
            # print(p1)
            # print(cw)
            document.add_paragraph(p1)
        # document.add_page_break()
    filename = title + '.docx'
    document.save('.\\dist\\' + filename)
    print('文件已保存在 ./dist/',filename)
    pass

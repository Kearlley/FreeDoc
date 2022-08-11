import json
import re
import time

from bs4 import BeautifulSoup

# re Pattern
import API.Request

keyPattern = re.compile(r'//.*', re.S)
keyPattern2 = re.compile(r'pay:.*,', re.S)
keyPattern3 = re.compile(r'<[^>]+>', re.S)


def Dump(html):
    Native = BeautifulSoup(html, "lxml")
    # print(Native)
    title = Native.find_all("h1")
    #print(title)
    title2 = re.sub(keyPattern3, '', str(title)).split('[')[1].split(']')[0]
    print(title2)
    # a = Native.select('script[type="text/javascript"]')
    a1 = re.compile(r"pic: (.*?)}$", re.MULTILINE | re.DOTALL)  # index pic
    # a0 = re.compile(r"//[\s\S]*?\n",re.MULTILINE | re.DOTALL)
    a = Native.find('script', text=a1)  # find script pos
    # print(a)

    a2 = a1.search(a.text).group(1)
    # data_json = json.loads('{' + a2 + '},}')
    # print(a2)
    a11 = a2.splitlines()
    # print(a11)

    a4 = []

    def buf():
        for lines in a11:
            # print(lines)
            try:
                a3 = re.sub(keyPattern, '', lines)
                # print(a3)
                a6 = re.sub(keyPattern2, '', a3)
                # print(a6)
                a8 = a6.split(':')[0]
                b1 = a6.split(':')[1]
                a7 = '"' + a8 + '"' + ':' + b1.replace("'", "\"")
                a4.append(a7)
            except:
                pass
                # print("Error!")
        return a4

    # Data jSon Up

    buflisttostr = ''.join(buf())
    buf2 = '{' + re.sub(re.compile('\s'), '', buflisttostr) + '}'
    #print(buf2)
    #print('-------------------------')

    # JSON
    bufj = json.loads(buf2)
    #print(bufj)
    #print('-------------------------')

    # to be json
    # a3 = buf2.split('{')[1]
    # a4 = a3.replace("'", "")
    # print(a4)

    # fs = open("Metadata", "w+", encoding='UTF-8')  # file

    # fs.write(a2)
    # fs.close()
    # fs = open("Metadata",'w', encoding='UTF-8').read()  # file
    # for line in fs:
    #    line2 = re.sub(keyPattern,'',line)
    #    print(line2)
    #    fs.write(line2)

    # fs.close()
    # print(data_json)

    # print('-------------------------')
    # matchPattern = re.compile(r'pay')
    # lineList = []

    # fs.close()

    # file = open('Metadata', 'r', encoding='UTF-8')
    # while 1:
    #    line = file.readline()
    #    if not line:
    #        print("Read End or Error")
    #        break
    #    elif matchPattern.search(line):
    #        pass
    #    else:
    #        lineList.append(line)

    # print('-------------------------')

    # fs = open(r'target.txt', 'w', encoding='utf-8')
    # for i in lineList:
    #    fs.write(i)
    # print('-------------------------')
    # fs.write('}')
    # fs.close()
    # outtmp = re.sub(keyPattern, ' ', a10)
    # print(outtmp)
    # outtmp = re.sub(keyPattern, ' ', a10)
    # fs = open("Metadata", "w+", encoding='UTF-8')  # file
    # fs.write(a10)
    # fs.close()
    # for file_ob in a2:
    # print(lines)
    # fs = open("Metadata", encoding='utf-8')
    # fs = fs.read()

    aid = bufj['aid']
    view_token = bufj['view_token']
    actual_page = bufj['actual_page']  # 全部页数
    preview_page = bufj['preview_page']  # 预览页数
    # print(aid)
    # print(view_token)
    # print(Tpage)
    # print(Ppage)
    project_id = 1
    return project_id, aid, view_token, actual_page, preview_page,title2


# def PageTask(actual_page, preview_page):
#    # HidePage = actual_page - preview_page
#    if actual_page == preview_page:
#        return True, preview_page
#    elif actual_page > preview_page:
#        return False, preview_page

def RequestImageUrl(project_id, aid, view_token, preview_page):
    print("Can Download Files: ",preview_page)
    # type(preview_page)
    # taskPage = int(preview_page) + 1
    buf = []
    for page in range(1, preview_page, 6):
        print("Url Getting... Now In ", str(page) + " -", str(page + 6))
        time.sleep(2)  # If to fast, can't get Url
        b1 = API.Request.RequestWebSite(
            "https://openapi.book118.com/getPreview.html"
            "?&project_id=" + project_id +
            "&aid=" + aid +
            "&view_token=" + view_token +
            "&page=" + str(page)
        )
        # b1
        # print(b1)
        json_data = re.search(r'jsonpReturn\((.*?)\);', b1).group(1)
        jsons = json.loads(json_data)
        urls = jsons['data']
        # print(urls)
        buf.append(urls)
    print('Done.')
    return buf

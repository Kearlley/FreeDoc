# 1. Download Files num, to cut url
import requests

from API import URL


def SaveFiles(Dict, type,FileFormat):
    page = 0
    # path = API.Public.GetWorkPath()
    # print("Download File Path In: ")
    for item in Dict:
        # print(item)
        page = page + 1
        # print(page)
        filename = str(page) + '.' + str(FileFormat)  # page.xxx
        if type is 'https':
            rd = requests.get(URL.NormalUrl(item))
            print(f'当前正在下载: {rd.url}' + f' 页数: {page}')
        else:
            rd = requests.get(item)
            print(f'当前正在下载: {rd.url}' + f' 页数: {page}')
        try:
            with open('.\\temp\\' + filename, 'wb') as temp:
                temp.write(rd.content)
        except IOError:
            print(f"下载错误，页数为: {page}")
    pass


def SaveFile(url, name, FileFormat):
    filename = name + '.' + FileFormat
    rd = requests.get(URL.NormalUrl(url))
    print(f'当前正在下载: {rd.url}')
    try:
        with open('.\\dist\\' + filename, 'wb') as temp:
            temp.write(rd.content)
    except IOError:
        print("下载失败")
    pass

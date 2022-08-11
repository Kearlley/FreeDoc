# 1. Download Files num, to cut url
import requests


def SaveFile(Dict):
    page = 0
    #path = API.Public.GetWorkPath()
    #print("Download File Path In: ")
    for items in Dict:
        for item in items.values():
            # print(item)
            page = page + 1
            # print(page)
            filename = str(page) + '.png'
            rd = requests.get('https:' + item)
            print('当前正在下载: ', rd.url + ' 页数: ', page)
            try:
                with open('.\\temp\\' + filename, 'wb') as temp:
                    temp.write(rd.content)
            except:
                print("下载错误，页数为:", page)
    pass

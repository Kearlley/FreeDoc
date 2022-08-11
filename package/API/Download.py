# 1. Download Files num, to cut url
import requests
import API.Public


def SaveFile(Dict):
    page = 0
    path = API.Public.GetWorkPath()
    print("Download File Path In: ", path)
    for items in Dict:
        for item in items.values():
            # print(item)
            page = page + 1
            # print(page)
            filename = str(page) + '.png'
            rd = requests.get('https:' + item)
            print('Now In Download: ', rd.url + ' Page: ', page)
            try:
                with open(path + '\\temp\\' + filename, 'wb') as temp:
                    temp.write(rd.content)
            except:
                print("Download has ERROR! At Page:", page)
    pass

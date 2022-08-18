import requests


def HeaderRequest(url,cookie):
    header = {  # Edge
        "Accept": "*/*",
        'DNT': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'
    }
    return requests.Session().get(url,headers=header,cookies=cookie).text
    pass


def RequestWebSite(url):
    # request.urlopen(url).read()
    return requests.Session().get(url).text
    pass

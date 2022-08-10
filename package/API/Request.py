import requests


def HeaderRequest(url):
    pass


def RequestWebSite(url):
    # request.urlopen(url).read()
    return requests.Session().get(url).text
    pass

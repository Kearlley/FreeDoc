class AC:
    def End(url):
        if str(url).strip('/'):
            return url
        else:
            return url + '/'

    def Start(url, *mode):
        if mode == 'http':
            return 'http://' + url
        if mode == 'https':
            return 'https://' + url


# Only Website Url
# mode = Url Use Request heard
def StandardizationUrl(url, *mode):
    el = str(url).encode('utf-8').lower()  # Operation Encode and To be lower case

    if el.startswith('http://') or el.startswith('https://'):
        AC.End(url)
    else:
        AC.Start(url)

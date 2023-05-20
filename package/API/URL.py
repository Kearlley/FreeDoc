from urllib.parse import urlparse, urlunparse


# mode = Url Use Request heard
def NormalUrl(url):
    print('原始URL：', url)
    # 将URL解析成6个部分，并进行小写化处理
    parsed_url = urlparse(url.lower())

    # 将路径部分进行小写化处理
    path = parsed_url.path.lower()

    # 将解析出来的6个部分重新组合成标准化的URL格式
    normalized_url = urlunparse((
        'https',
        parsed_url.netloc,
        path,
        parsed_url.params,
        parsed_url.query,
        parsed_url.fragment
    ))
    print('标准化后URL：', normalized_url)
    return normalized_url

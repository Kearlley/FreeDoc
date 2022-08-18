# Test Data Line
import json
import re

import tqdm

import API
from API import Request


# Test Data Line End
from Method import BaiduWenKu


def main(url):
    cks = BaiduWenKu.ReadCookies()
    c3 = BaiduWenKu.Dump(
        API.Request.HeaderRequest(
            url, cks
        )
    )
    print(c3)
    pass


if __name__ == '__main__':
    main('')

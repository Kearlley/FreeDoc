import os

import API.Request
import API.Download
import Method.YuanChuangLi
import API.MergeFile

from Public import *


def main():
    try:
        os.mkdir('.\\temp')
        os.mkdir('.\\dist')
    except:
        pass
    StartInfo()
    url = input("请键入你要下载的文档链接:")
    # print(API.Request.RequestWebSite("https://openapi.book118.com/getPreview.html?&project_id=1&aid=423296707&view_token=UBtcTIq@V8U3kwlXPT_HlrdCyv_rgeV7&page=5"))
    c1 = Method.YuanChuangLi.Dump(
        API.Request.RequestWebSite(
            url
        )
    )
    print('共计 %s 页' % c1[3])
    API.Download.SaveFile(
        Method.YuanChuangLi.RequestImageUrl(
            str(c1[0]),
            str(c1[1]),
            str(c1[2]),
            int(c1[4])
        )
    )
    API.MergeFile.ToPDF(c1[5])

    pass


if __name__ == '__main__':
    main()
    time.sleep(5)

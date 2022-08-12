import os

import API.Request
import API.Download
import API.MergeFile

from Method import YuanChuangLi, GDJYCBSCPXXJSXT
from Public import *


def main():
    try:
        os.mkdir('.\\temp')
        os.mkdir('.\\dist')
    except:
        pass
    StartInfo()
    # bufs = ''
    url = input("请键入你要下载的文档链接: ")
    match AnalyzeURL(url):
        case 0:  # 原创力
            c1 = YuanChuangLi.Dump(
                API.Request.RequestWebSite(
                    url
                )
            )
            # print(API.Request.RequestWebSite("https://openapi.book118.com/getPreview.html?&project_id=1&aid=423296707&view_token=UBtcTIq@V8U3kwlXPT_HlrdCyv_rgeV7&page=5"))
            print('共计 %s 页' % c1[3])
            API.Download.SaveFiles(
                YuanChuangLi.RequestImageUrl(
                    str(c1[0]),  # project_id
                    str(c1[1]),  # aid
                    str(c1[2]),  # view_token
                    int(c1[4])  # preview_page
                )
            )
            API.MergeFile.ToPDF(c1[5])
            # bufs.append(c1)
            pass
        case 1:  # 高等教育出版社产品信息检索系统
            c2 = GDJYCBSCPXXJSXT.Dump(
                API.Request.RequestWebSite(
                    url
                )
            )
            API.Download.SaveFile(
                c2[1],  # URL
                c2[0]  # title
            )
            print('pdf文件已经保存在 ./dist/ 目录下！')
            pass


if __name__ == '__main__':
    main()
    time.sleep(10)  # Wait 10s Exit

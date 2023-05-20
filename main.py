import time

import API.Download
import API.MergeFile
import API.Request
from Method import YuanChuangLi, GDJYCBSCPXXJSXT
from Public import *

maekdirs = [
    'temp',
    'dist',
    'cookies'
]


def main():
    MakeBaseDir(maekdirs)
    StartInfo()
    # bufs = ''
    url = input("请键入你要下载文档的页面链接: ")
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
                ), 'pdf'
            )
            API.MergeFile.TempToPDF(c1[5])
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
                c2[0],  # title
                'pdf'  # Format
            )
            print('pdf文件已经保存在 ./dist/ 目录下！')
            pass
        case 2:  # 百度文库
            cks = BaiduWenKu.ReadCookies()
            c3 = BaiduWenKu.Dump(
                API.Request.HeaderRequest(
                    url, cks
                )
            )
            print('文档标题为:', c3[0])  # title
            print('文档页数为:', c3[1])  # page
            # print('NativeIndexData:\n', c3[3])  # Index
            match c3[2]:
                case 'word':
                    print('文件类型为: Word')
                    BaiduWenKu.Doc_RePage(
                        BaiduWenKu.GetPageIndexUrl(
                            c3[3]
                        )[0],
                        title=c3[0]
                    )
            pass
        case 9998:  # Save Cookies
            print(
                '1. baidu',
            )
            cb = input('请输入你想保存的Cookies所对应的数字: ')
            # webbrs = input('请输入你想使用的浏览器驱动{edge,firefox,chrome}: ')  # TODO
            match cb:
                case 1:
                    BaiduUsername = input('请输入你的百度账号的 手机/用户名/邮箱:')
                    BaiduPassword = input('请输入你的百度账号的 密码:')
                    BaiduWenKu.SaveCookies(BaiduUsername, BaiduPassword)
        case 9999:  # Cookies
            CookiesInfo()
            pass


if __name__ == '__main__':
    main()
    time.sleep(15)  # Wait 15s Exit

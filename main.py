import API.Request
import API.Download
import Method.YuanChuangLi

from Public import *


def main():
    StartInfo()
    # print(API.Request.RequestWebSite("https://openapi.book118.com/getPreview.html?&project_id=1&aid=423296707&view_token=UBtcTIq@V8U3kwlXPT_HlrdCyv_rgeV7&page=5"))
    c1 = Method.YuanChuangLi.Dump(
        API.Request.RequestWebSite(
            "https://max.book118.com/html/2022/0622/5133034111004244.shtm"
        )
    )
    API.Download.SaveFile(Method.YuanChuangLi.RequestImageUrl(str(c1[0]),str(c1[1]),str(c1[2]),int(c1[4])))
    pass


if __name__ == '__main__':
    main()

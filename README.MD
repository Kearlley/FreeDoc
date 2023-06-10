# FreeDoc Download - developing

## 支持
- 原创力免费预览部分(https://max.book118.com)
- 高等教育出版社信息检索系统样章阅读部分(https://xuanshu.hep.com.cn/)
- 百度文库-文档(https://wenku.baidu.com/)
- 豆丁网(https://www.docin.com/)
## 提示
- 目前版本(百度文库下载功能)需要去下载 **[msedgedriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)**(在较下面可以看到) 来完成cookies获取操作
- 请确保你所下载的 msedgedriver 的版本和浏览器一致，在下载好后请放在项目或编译结果同级的 driver 目录中
- 如果你是直接使用 Python 来运行 main.py 可能需要修改一下源码中的部分路径(或者自己手动创建)，因为目前主要是以编译为主写的代码，所以可能会有一些路径问题
- 对于Linux平台的，需要修改 package->Method->BaiduWenku.py->option.binary_location 的变量来指定你的浏览器目录，以及对应的浏览器driver版本，来确保Cookies获取模块的正常运行.
- 目前项目代码以及变量名有点混乱，~~可能有空了会去重构(咕咕咕~~
## 运行
```shell
git clone https://github.com/Kearlley/FreeDoc.git
cd ./FreeDoc
python main.py
```
## 编译
```shell
git clone https://github.com/Kearlley/FreeDoc.git
cd ./FreeDoc
python setup.py
```
然后就可以去 **dist** 找到可执行文件
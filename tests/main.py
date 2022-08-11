import os


def TestMain():
    print(os.path.split(os.path.realpath('.'))[0])  # 获取当前工作目录路径
    pass


if __name__ == '__main__':
    TestMain()

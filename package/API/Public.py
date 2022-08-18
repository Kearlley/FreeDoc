import os


def GetWorkPath(): return os.path.split(os.path.realpath('.'))[0] + "\\" + os.path.split(os.path.realpath('.'))[1]  # 获取当前工作目录路径

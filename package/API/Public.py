import os


def GetWorkPath(): return os.path.split(os.path.realpath('.'))[0]  # 获取当前工作目录路径

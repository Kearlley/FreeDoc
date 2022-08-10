# -*- coding: UTF-8 -*-
import time


# mode = Return Style
def GetTime(mode):
    NA = time.time()
    match mode:
        case 0:  # Native Time
            return NA
        case 1:  # Native Local Time
            return time.localtime(NA)
        case 2:
            return time.strftime("%Y-%m-%d | %H:%M:%S")
        case 3:
            return time.strftime("%Y %a %b %d | %H:%M:%S")
        case 4:
            return "N/A"


def StartInfo():
    print(
        """
📕FreeDoc Download
🎯Support: 原创力
🕙Time: %s
----------------------------------
"""
        % GetTime(2)
    )

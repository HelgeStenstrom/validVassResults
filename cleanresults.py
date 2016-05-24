# -*- coding:utf-8 -*-

import re


def foo():
    return "bar"


def validateTolName(name):
    if re.match("\d_152_82-LPA_109_332_1-\d{1,3}", name):
        return True
    return False


def validateTimeStampName(ts):
    try:
        (year, month, day, hour, minute, sec) = re.match("(\d\d\d\d)(\d\d)(\d\d)_(\d\d)(\d\d)(\d\d)", ts).groups()
    except AttributeError:
        return False
    if (2000 < int(year) < 2050) and (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
        if (0 <= int(hour) <= 23) and (0 <= int(minute) <= 59) and (0 <= int(sec) <= 59):
            return True
    return False

def essentialFile(name):
    return name =="28740.69729W.csv"


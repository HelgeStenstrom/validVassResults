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


def isTestCaseId(id):
    try:
        tc = int(id)
    except ValueError:
        return False
    return 10000 < tc < 99999


def isTestCaseSetId(id):
    try:
        tcs = int(id)
    except ValueError:
        return False
    return 10000 < tcs < 99999


def isWFile(name):
    try:
        return NameParts(name).ShortName == "W" and NameParts(name).suffix == "csv"
    except ValueError:
        return False

def isInteresting(name):
    tests = [isWFile]
    verdicts = [test(name) for test in tests]
    return True in verdicts

def onePredicateFilled(nameList, predicate):
    verdicts = [predicate(n) for n in nameList]
    return True in verdicts

class NameParts:
    def __init__(self,name):
        pattern = re.compile("(\d*)(.*)\.(\d*)\_*(\d*)(.*)\.(.*)")
        try:
            p1, p2, p3, p4, p5, p6 = pattern.search(name).groups()
            self.tc = p1
            self.OneLetter = p2
            self.tcs = p3
            self.loopnum = p4
            self.ShortName = p5
            self.suffix = p6
        except AttributeError:
            raise ValueError



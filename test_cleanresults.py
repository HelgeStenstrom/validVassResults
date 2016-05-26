#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cleanresults as c


import unittest

# =====  Unit tests start here ==========



class ValidateTests(unittest.TestCase):
    def testTolDirName(self):
        self.assertFalse(c.validateTolName('notATolName'))
        self.assertTrue(c.validateTolName('2_152_82-LPA_109_332_1-906'))

    def testTimeStampName(self):
        self.assertTrue(c.validateTimeStampName("20151209_155523"))
        self.assertFalse(c.validateTimeStampName(""))
        self.assertFalse(c.validateTimeStampName("12341212_121212"))
        self.assertFalse(c.validateTimeStampName("20160101_120160"))
        self.assertTrue(c.validateTimeStampName("20160101_120159"))

    def testEssentialFiles(self):
        self.assertFalse(c.essentialFile("spam"))
        self.assertTrue(c.essentialFile("28740.69729W.csv"))

    def testIsTCNum(self):
        self.assertTrue(c.isTestCaseId("28740"))
        self.assertTrue(c.isTestCaseId("28741"))
        self.assertFalse(c.isTestCaseId(""))
        self.assertFalse(c.isTestCaseId("abc"))


    def testIsTCSNum(self):
        self.assertTrue(c.isTestCaseSetId("69729"))
        self.assertTrue(c.isTestCaseSetId("12345"))
        self.assertFalse(c.isTestCaseSetId(""))
        self.assertFalse(c.isTestCaseSetId("abc"))

    def testIsWFile(self):
        self.assertTrue(c.isWFile("28740.69729W.csv"))
        self.assertTrue(c.isWFile("1.1W.csv"))
        self.assertFalse(c.isWFile("28740.69729L.csv"))
        self.assertFalse(c.isWFile(""))


class NamePartsTests(unittest.TestCase):
    def testNameParts(self):
        name = "28740.69729Alarmw.txt"
        result = c.NameParts(name)
        self.assertEqual("28740", result.tc)
        self.assertEqual("", result.OneLetter)
        self.assertEqual("69729", result.tcs)
        self.assertEqual("Alarmw", result.ShortName)
        self.assertEqual("txt", result.suffix)


    def testNameParts2(self):
        name = "30431.74123_1Log.txt"
        result = c.NameParts(name)
        self.assertEqual("30431", result.tc )
        self.assertEqual("", result.OneLetter)
        self.assertEqual("74123", result.tcs)
        self.assertEqual("1", result.loopnum)
        self.assertEqual("Log", result.ShortName)
        self.assertEqual("txt", result.suffix )


if __name__ == '__main__':
    unittest.main()

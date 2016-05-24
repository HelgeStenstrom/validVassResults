#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cleanresults as c


import unittest

# =====  Unit tests start here ==========


class SomeTests(unittest.TestCase):

    def testPass(self):
        """Always pass"""
        pass

    def testSomething(self):
        """Run a function"""
        c.foo()
        self.assertEquals(1, 1)

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


if __name__ == '__main__':
    unittest.main()

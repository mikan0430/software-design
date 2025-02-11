#!/usr/bin/python3

import unittest
from calc_mul import calc
import sys

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        #追加分

        def test_sample5 (self):
                self.assertEqual (-1, calc(1000,150))

        def test_sample6 (self):
                self.assertEqual (150, calc(1,150))

        def test_sample7 (self):
                self.assertEqual (149850, calc(999,150))

        def test_sample8 (self):
                self.assertEqual (-1, calc(sys.maxsize,sys.maxsize))

        def test_sample9 (self):
                self.assertEqual (-1, calc("1","100"))
        
        

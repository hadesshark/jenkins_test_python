# -*- coding:utf-8 -*-
import unittest

import foo

class SimpleTest(unittest.TestCase):
    """
    測試做除法的函數
    """
    def test1(self):
        self.assertEqual(foo.divide(2, 2), 1)

    def test2(self):
        self.assertEqual(foo.divide(0, 1), 1)

if __name__ == "__main__":
    unittest.main()

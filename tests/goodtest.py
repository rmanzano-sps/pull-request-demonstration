#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Lesson 07 task 01."""


# Import Python libs
import unittest


# Import user libs
import good_file


class GoodFileTestCase(unittest.TestCase):
    """GoodFile tests"""


    def test_bool_val(self):
        """Tests that BOOL_VAL is true"""
        assertTrue(good_file.BOOL_VAL)


if __name__ == '__main__':
    unittest.main()

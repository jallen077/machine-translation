"""This file is used to test the Language Translator Functions"""

import unittest

from translator import english_to_french, english_to_german

class TestFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("This is a test."),"C'est un test.")
        self.assertNotEqual(english_to_french("These lines are not equal"),"Pickle")
        self.assertTrue(english_to_french("Test"))
        

class TestGerman(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_german("Hello"),"Hello")
        self.assertEqual(english_to_german("This is a test."),"Tá sé seo le tástáil.")
        self.assertNotEqual(english_to_german("These lines are not equal"),"Pickle")
        self.assertTrue(english_to_german("Test"))

unittest.main()

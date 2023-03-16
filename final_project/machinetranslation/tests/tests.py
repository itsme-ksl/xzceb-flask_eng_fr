"""Run from command line:
$ python -m unittest tests/test_translator.py
"""

import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Test tranlation from English to French using IBM Watson API.
    """
    def test1(self):
        """
        Test of the function english_to_french.
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Hello")

class TestFrenchToEnglish(unittest.TestCase):
    """
    Test tranlation from French to English using IBM Watson API.
    """
    def test1(self):
        """
        Test of the function french_to_english.
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

if __name__ == '__main__':

    unittest.main()
    
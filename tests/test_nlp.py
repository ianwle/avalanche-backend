# -*- coding: utf-8 -*-

from .context import project
from project.project.nlp_methods import *

import unittest


class BasicNlpTestSuite(unittest.TestCase):
    """Basic NLP preprocessing test cases."""

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase("Capitalized sentence"), "capitalized sentence")

    def test_to_tokens(self):
        self.assertEqual(to_tokens("My father caught a fish"),
                         ["My", "father", "caught", "a", "fish"])

    def test_to_no_whitespace(self):
        self.assertEqual(to_no_whitespace("This  has extra whitespace"), "This has extra whitespace")
    
    def test_to_correct_spelling(self):
        self.assertEqual(to_correct_spelling(["confuson", "matix"]), ["confusion", "matrix"])
    
    # def test_to_no_stopwords(self):
        # self.assertEqual(to_no_stopwords(""), "")
        pass
        
    def test_to_no_punctuation(self):
        pass
    
    def test_to_lemmatized(self):
        pass
    
    def test_to_stemmed(self):
        pass
    
    def test_to_no_tags(self):
        pass
    
    def test_to_no_url(self):
        pass
    
if __name__ == '__main__':
    unittest.main()

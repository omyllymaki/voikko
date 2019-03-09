import json
import unittest

import requests

URL = 'http://localhost:8000/lemmatize'


class TestLemmatization(unittest.TestCase):

    def test_baseform_should_return_baseform(self) -> None:
        tokens = ['juosta']
        actual = get_response(tokens)
        expected = {'juosta': ['juosta']}
        self.assertEqual(actual, expected)

    def test_singular_should_return_baseform(self) -> None:
        tokens = ['juokseminen']
        actual = get_response(tokens)
        expected = {'juokseminen': ['juosta']}
        self.assertEqual(actual, expected)

    def test_unrecognized_word_should_return_empty_list(self) -> None:
        tokens = ['juokseminenn']
        actual = get_response(tokens)
        expected = {'juokseminenn': []}
        self.assertEqual(actual, expected)

    def test_multiple_words_should_return_baseforms(self) -> None:
        tokens = ['juosta', 'juokseminen', 'koiraa', 'venee']
        actual = get_response(tokens)
        expected = {'juosta': ['juosta'], 'juokseminen': ['juosta'], 'koiraa': ['koira'], 'venee': []}
        self.assertEqual(actual, expected)


def get_response(tokens):
    data = {'tokens': tokens}
    result = requests.post(URL, json.dumps(data))
    response = json.loads(result.text)
    return response

import unittest

import requests


class TestApi(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/wiki"

    def test_search_python(self):
        # testing standard answer if article found - return 200
        url = "http://127.0.0.1:5000/wiki/python"
        response = requests.get(url, headers={"Accept-Language": "en"})
        self.assertEqual(response.status_code, 200, "API did not return a successful response")

    def test_search_nonexistent_term(self):
        # error 404 if no article found
        language = "en"
        search_term = "dsfdfgdrgkdkruzghfg"

        url = f"{self.base_url}/{search_term}?lang={language}"
        response = requests.get(url, headers={"Accept-Language": language})

        self.assertEqual(response.status_code, 404, "API did not return a 404 response for a nonexistent term")

if __name__ == '__main__':
    unittest.main()
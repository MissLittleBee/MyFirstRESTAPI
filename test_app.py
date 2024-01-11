import unittest
import requests
from api import app

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

    def test_search_rumbellion_in_czech(self):
        # testing the "word"" isn´t the same, but exist in another article - return 303
        language = "cs"
        search_term = "rumbellion"

        url = f"{self.base_url}/{search_term}?lang={language}"
        response = requests.get(url, headers={"Accept-Language": language})

        self.assertEqual(response.status_code, 303,
                         "API did not return a 303 response for a term present in other articles")

        # Check if the response contains some articles (optional, depends on API implementation)
        data = response.json()
        self.assertTrue('articles' in data and len(data['articles']) > 0, "API did not return any articles")


if __name__ == '__main__':
    unittest.main()
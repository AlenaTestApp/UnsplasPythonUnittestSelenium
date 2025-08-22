import unittest
from toolkit.base_case import BaseCase
from config import *


class SearchFilter(BaseCase):

    def test_search_result(self):
        """UC-AUTH-03-01: Verify that Search query entered by User is
        correctly displayed on the Result page. Backend Data match the entered keyword
        Request: https://api.unsplash.com/search/photos?query=flowers&per_page=10"""
        query = "flowers"
        matches = 0
        # Check Web: search by query
        self.unsplash.search_page.search_by_query(query)
        # Make API request, retrieve data for 10 pages and analyze result. Test passes
        # if at least 5 results contains the query word in picture description
        status, data = self.unsplash.search_page.make_request(SEARCH_BY_QUERY_ENDPOINT, "flowers", 10)
        if status == 200:
            matches = self.unsplash.search_page.check_result(data, query)
        self.assertGreaterEqual(matches, 5, f"Expected at least 5 results with {query}, but got {matches}")




if __name__ == "__main__":
    unittest.main()
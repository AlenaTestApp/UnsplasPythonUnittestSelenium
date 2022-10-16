import unittest
from toolkit.base_case import BaseCase
from config import *


class uiTesting(BaseCase):
    def test_1_get_title(self):
        """Assert Page title is correct"""
        print(self.tripadvisor.home_page.get_title())
        assert self.tripadvisor.home_page.get_title() == page_title

    def test_2_check_logo(self):
        """Assert Logo is displayed"""
        assert self.tripadvisor.home_page.check_logo() is True

    def test_3_user_login(self):
        """Validate User is able to Log in and User's nickname is in current URL"""
        self.tripadvisor.home_page.user_login(user_email, user_pwd)
        self.assertEqual(self.tripadvisor.home_page.check_nickname(), nick_name)


if __name__ == '__main__':
    unittest.main()

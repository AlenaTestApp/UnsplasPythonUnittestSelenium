import time
import unittest
from toolkit.base_case import BaseCase
from config import *


class uiTesting(BaseCase):
    def test_1_get_title(self):
        """Assert Page title is correct"""
        self.assertEqual(self.unsplash.home_page.get_title(), PAGE_TITLE)

    def test_2_check_logo(self):
        """Assert Logo is displayed"""
        self.assertTrue(self.unsplash.home_page.check_logo())

    def test_3_user_login(self):
        """Validate User is able to Log in and User's nickname is correctly
        displayed on Account Page"""
        self.unsplash.home_page.user_login(USER_EMAIL, USER_PWD)
        self.assertEqual(self.unsplash.home_page.check_nickname(), NICK_NAME)
        self.unsplash.home_page.user_logout()

    def test_4_email_server_validation(self):
        """Validate 'Invalid email or password' error message while
        Login with non-existing or too long email"""

        server_cases = [c for c in INVALID_LOGIN_CASES if c["id"] in ("non_existing_email", "too_long_email")]
        for case in server_cases:
            with self.subTest(id=case["id"]):
                email = case["email"]
                error_message = self.unsplash.home_page.invalid_login_server_validation(email, USER_PWD)
                self.assertEqual(error_message, LOGIN_ERR, f"No Error message is displayed for {email} with case id {case['id']}")
                self.driver.refresh()

    def test_5_email_browser_validation(self):
        """Validate browser rejects invalid emails even before submitting the Login form"""
        browser_cases = [c for c in INVALID_LOGIN_CASES if c["id"] != "too_long_email" and c["id"] != "non_existing_email"]
        for case in browser_cases:
            with self.subTest(id=case["id"]):
                email = case["email"]
                is_valid = self.unsplash.home_page.invalid_login_browser_validation(email, USER_PWD)
                self.assertFalse(is_valid, f"Email {email} with case id {case['id']} unexpectedly passed validation.")

    def test_6_login_with_empty_fields(self):
        """Validate 'Invalid email or password' error message while
        Login with empty[combinations] email/password fields"""
        empty_cases = [{"email": "", "password": USER_PWD},
                       {"email": USER_EMAIL, "password": ""},
                       {"email": "", "password": ""}]
        for indx, case in enumerate(empty_cases, start=1):
            with self.subTest(id=f"case_id_{indx}"):
                email = case["email"]
                password = case["password"]
                error_message = self.unsplash.home_page.invalid_login_server_validation(email, password)
                self.assertEqual(error_message, LOGIN_ERR,
                                 f"No Error message is displayed for case id {indx} email {email} password {password}")
                self.driver.refresh()

    def test_7_user_logout(self):
        """Test validates successful log out: User is redirected to Home Page
        after clicking on Logout button, URL should contain 'logged out'"""
        self.unsplash.home_page.user_login(USER_EMAIL, USER_PWD)
        url = self.unsplash.home_page.user_logout()
        self.assertIn(LOGOUT_CONF, url.lower(), f"'logged out' should be in URL, {url} instead")




if __name__ == '__main__':
    unittest.main()

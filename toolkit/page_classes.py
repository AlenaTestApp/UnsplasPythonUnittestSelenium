
from toolkit.locators import Locators
from toolkit.element import BasePageElement
from config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from toolkit.healing import heal_find
import requests


class UnSplash:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)
        self.search_page = SearchPage(self.driver)


class BasePage(object):
    login_email = BasePageElement(Locators.EMAIL)
    login_password = BasePageElement(Locators.PASSWORD)
    search_field = BasePageElement(Locators.SEARCH_FIELD)

    def __init__(self, driver):
        self.driver = driver

    def wait(self, *element, tm=2):
        wait = WebDriverWait(self.driver, tm)
        wait.until(lambda driver: self.driver.find_element(*element))
        return self.driver.find_element(*element)


class HomePage(BasePage):

    def get_title(self):
        """Method returns tripadvisor page title"""
        page_ttl = self.driver.title.split(':')[0]
        return page_ttl

    def check_logo(self):
        """Returns True if Logo is displayed"""
        self.wait(*Locators.LOGO)
        return self.driver.find_element(*Locators.LOGO).is_displayed()

    def user_login(self, email, password):
        """Method performs User Login"""
        if self.driver.current_url == HOME_PAGE:
            self.wait(*Locators.LOGIN_HOME).click()
            self.login_email = email
            self.login_password = password
            self.driver.find_element(*Locators.LOGIN_SUBMIT).click()

    def check_nickname(self):
        """Method verifies nickname of logged-in User,
        navigates User to Profile page, returns nickname text that displayed next to
        Avatar Picture"""
        self.go_to_account()
        nikname = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.NIK_NAME)).text
        return nikname


    def go_to_account(self):
        """Logged in User clicks on Profile Avatar Picture and navigates to User Account.
        Asserts that URL formed correctly: contains nikname"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE_PICTURE))
        self.driver.find_element(*Locators.PROFILE_PICTURE).click()
        self.wait(*Locators.VIEW_PROFILE).click()
        current_url = self.driver.current_url
        assert NICK_NAME.lower() in current_url


    def invalid_login_server_validation(self, email, password):
        """Function perform Login attempt with Invalid Users credentials. Reads Error message"""
        if self.driver.current_url == HOME_PAGE:
            self.wait(*Locators.LOGIN_HOME).click()

        email_field = self.wait(*Locators.EMAIL)
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.wait(*Locators.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

        self.driver.find_element(*Locators.LOGIN_SUBMIT).click()
        login_error = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(Locators.LOGIN_ERROR)).text
        return login_error


    def invalid_login_browser_validation(self, email, password):
        """Function attempts to log in with invalid credentials and
        validate the browser built-in HTML5 rules. Return false if email input invalid/True otherwise"""
        self.wait(*Locators.LOGIN_HOME).click()
        self.login_email = email
        self.login_password = password
        email_el = self.driver.find_element(*Locators.EMAIL)
        is_valid = email_el.get_property("validity")["valid"]
        return is_valid


    def user_logout(self):
        """Function clicks on Logout button on Profile Picture.
         After User is redirected to Home screen, returns Page URL"""
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(Locators.PROFILE_PICTURE))
        self.driver.find_element(*Locators.PROFILE_PICTURE).click()
        logout = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.LOGOUT_BTN))
        logout.click()
        logged_out = self.driver.current_url
        return logged_out


class SearchPage(BasePage):


    def search_by_query(self, query):
        # self.wait(*Locators.SEARCH_FIELD)
        # self.search_field = query + Keys.ENTER
        # Trying the self-healing locators strategy
        search_field = heal_find(self.driver,
                                 primary=Locators.SEARCH_FIELD,
                                 fallbacks=Locators.SEARCH_FIELD_FALLBACK,
                                 intent=Locators.SEARCH_FIELD_INTENT)
        search_field.clear()
        search_field.send_keys(query + Keys.ENTER)

    def make_request(self, url: str, query: str, per_page: int):
        """Request to Unsplash server, returns status code, query relevant data
        for number of pages specified in parameters"""
        r = requests.get(
            url,
            params={"query": query, "per_page": per_page},
            headers={"Authorization": f"Client-ID {ACCESS_KEY}"},
            timeout=20,
        )
        return r.status_code, r.json()

    def check_result(self, data, query):
        """Check API response and count the results containing query in picture description"""
        res_count = 0
        for item in data["results"]:
            description = item.get("description") or item.get("alt_description") or item.get("slag") or ""
            if query.lower() in description.lower():
                res_count += 1
        return res_count






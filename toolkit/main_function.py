import time

from toolkit.locators import Locators
from toolkit.element import BasePageElement
from config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UnSplash:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)


class BasePage(object):
    login_email = BasePageElement(Locators.EMAIL)
    login_password = BasePageElement(Locators.PASSWORD)

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
        assert nick_name.lower() in current_url


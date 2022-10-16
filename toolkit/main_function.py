from toolkit.locators import Locators
from toolkit.element import BasePageElement
from config import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TripAdvisor:
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
        return self.driver.find_element(*Locators.LOGO).is_displayed()

    def user_login(self, email, password):
        """Method performs User Login"""
        if self.driver.current_url == HOME_PAGE:
            self.wait(*Locators.SIGNIN).click()
            iframe = self.wait(*Locators.IFRAME)
            self.driver.switch_to.frame(iframe)
            self.driver.find_element(*Locators.CONT_WITH_EMAIL).click()
            self.login_email = email
            self.login_password = password
            self.driver.find_element(*Locators.LOGIN).click()
            WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located(Locators.IFRAME))
            self.driver.switch_to.default_content()

    def check_nickname(self):
        """Method verifies nickname of logged-in User,
        navigates User to Profile page, returns nickname taken from current URL"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE_PICTURE))
        self.driver.find_element(*Locators.PROFILE_PICTURE).click()
        self.wait(*Locators.VIEW_PROFILE).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.AVATAR))
        return self.driver.current_url.split('/')[-1]


from selenium.webdriver.common.by import By
from config import *


class Locators(object):

    # Home Page Login Locators
    LOGO = (By.CSS_SELECTOR, "a[title='Home — Unsplash'] svg")
    LOGIN_HOME = (By.XPATH, "//a[contains(@href, '/login')]")
    CONT_WITH_EMAIL = (By.CSS_SELECTOR, "#ssoButtons > button > span.textContainer")
    EMAIL = (By.XPATH, "//input[@name = 'email']")
    PASSWORD = (By.XPATH, "//input[@name = 'password']")
    LOGIN_SUBMIT = (By.XPATH, "//button[contains(text(), 'Login')]")
    PROFILE_PICTURE = (By.XPATH, f"//img[contains(@alt, {NICK_NAME})]")
    VIEW_PROFILE = (By.XPATH, "//span[contains(text(), 'View profile')]")
    NIK_NAME = (By.XPATH, "//a[contains(text(), 'Edit profile')]/ancestor::div[1]/preceding-sibling::div[1]")
    LOGIN_ERROR = (By.XPATH, "//button[@type='button']/preceding::p")
    LOGOUT_BTN = (By.XPATH, "//span[contains(text(), 'Logout')]")
    LOGOUT_CONFIRMATION = (By.XPATH, "/div/p[contains(text(), 'Successfully logged out')]") # TBD


    # Search Page
    SEARCH_FIELD = (By.XPATH, "//input[@type = 'Search']")  # <- intended typo to check selfhealing locators: worked!
    SEARCH_FIELD_FALLBACK = (By.XPATH, "//input[@placeholder = 'Search photos and illustrations']")
    SEARCH_FIELD_INTENT = {
        "attrs": {
            "type": "search",
            "title": "Search Unsplash"
        }
    }


import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config import *
from toolkit.main_function import TripAdvisor
import time
import os


class BaseCase(unittest.TestCase):
    driver = None
    tripadvisor = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.tripadvisor = TripAdvisor(cls.driver)
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')

    def setUp(self):
        self.driver.get(HOME_PAGE)

    def tearDown(self):
        filename = self._testMethodName + '_' + time.strftime('%T') + "_" + time.strftime('%Y') + '.png'
        if self._test_failed():
            self.driver.save_screenshot(r"screenshots/" + filename)

    @classmethod
    def tearDownClass(cls):
        del cls.tripadvisor
        cls.driver.quit()

    def _test_failed(self):
        for method, error in self._outcome.errors:
            if error:
                return True
        return False

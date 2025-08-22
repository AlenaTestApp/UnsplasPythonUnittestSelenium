import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config import *
from toolkit.page_classes import UnSplash
import time
import os



class BaseCase(unittest.TestCase):
    driver = None
    unsplash = None

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver = webdriver.Chrome()
        cls.unsplash = UnSplash(cls.driver)
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
        del cls.unsplash
        cls.driver.quit()

    def _test_failed(self):
        for method, error in self._outcome.errors:
            if error:
                return True
        return False


from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    locator = None

    def __init__(self, locator):
        self.locator = locator

    def __set__(self, obj, value):
        """ Sets the text to the value supplied """
        driver = obj.driver
        WebDriverWait(driver, 3).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """ Gets the text of the specified object """
        driver = obj.driver
        WebDriverWait(driver, 3).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")
        # return element.text


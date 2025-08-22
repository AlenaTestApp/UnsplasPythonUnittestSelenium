from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def heal_find(driver, primary=None, fallbacks=None, intent=None):
    # Primary
    if primary:
        try:
            return driver.find_element(*primary)
        except NoSuchElementException:
            pass

    # Fallbacks
    if fallbacks:
        if fallbacks:
            if isinstance(fallbacks, tuple) and len(fallbacks) == 2:
                fallbacks = [fallbacks]
            for loc in fallbacks:
                try:
                    return driver.find_element(*loc)
                except NoSuchElementException:
                    pass
    raise NoSuchElementException(f"Element not found: {primary}, {fallbacks}, {intent}")

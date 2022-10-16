from selenium.webdriver.common.by import By


class Locators(object):

    # Home Page Locators
    LOGO = (By.XPATH, "//img[@alt = 'Tripadvisor']")
    SIGNIN = (By.XPATH, "//span[contains(text(), 'Sign in')]")
    IFRAME = (By.XPATH, "//iframe[@title = 'regcontroller']")
    CONT_WITH_EMAIL = (By.CSS_SELECTOR, "#ssoButtons > button > span.textContainer")
    EMAIL = (By.ID, "regSignIn.email")
    PASSWORD = (By.ID, "regSignIn.password")
    LOGIN = (By.XPATH, "//*[@id='regSignIn']/div[4]/button[1]")
    PROFILE_PICTURE = (By.XPATH, "//a[@aria-label = 'Profile']/div/div/div/picture")
    VIEW_PROFILE = (By.XPATH, "//span[contains(text(), 'View profile')]")
    AVATAR = (By.XPATH, "//span/img[contains(@src, 'avatar')][1]")

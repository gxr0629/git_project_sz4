from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, timeout=10, poll=1):
        by, value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(by, value))

    def find_elements(self, location, timeout=10, poll=1):
        by, value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(by, value))

    def click(self, location):
        self.find_element(location).click()

    def send_keys(self, location, text):
        self.find_element(location).send_keys(text)

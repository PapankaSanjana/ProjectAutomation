import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//button[text()='Login']")

    def _login_form_present(self):
        elements = self.driver.find_elements(*self.EMAIL)
        return bool(elements and elements[0].is_displayed())

    def login(self, email, password):
        if not self._login_form_present():
            login_url = self.driver.current_url.rstrip('/') + '/login'
            self.driver.get(login_url)
            WebDriverWait(self.driver, 30).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
        self.type(self.EMAIL, email, timeout=30)
        self.type(self.PASSWORD, password, timeout=30)
        self.click(self.LOGIN_BTN)
        time.sleep(2)
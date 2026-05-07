from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def is_home_loaded(self):

        try:

            # wait for complete page load
            WebDriverWait(self.driver, 40).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

            # wait for URL change after login
            WebDriverWait(self.driver, 40).until(
                lambda d: "login" not in d.current_url.lower()
            )

            # wait for visible body
            WebDriverWait(self.driver, 40).until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )

            print("Current URL:", self.driver.current_url)

            return True

        except Exception as e:

            print("HOME PAGE LOAD FAILED")
            print(e)

            return False

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config_reader import get_config


def test_login(driver):

    config = get_config()

    driver.get(config["base_url"])

    # wait for initial page load
    WebDriverWait(driver, 40).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    login = LoginPage(driver)

    login.login(
        config["email"],
        config["password"]
    )

    # wait for login redirect
    WebDriverWait(driver, 40).until(
        lambda d: "login" not in d.current_url.lower()
    )

    # wait for body visible
    WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    )

    home = HomePage(driver)

    assert home.is_home_loaded(), "Home page failed to load after login"

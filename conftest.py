import pytest

from fixtures.browser_fixture import get_driver


@pytest.fixture(scope="function")
def driver():

    driver = get_driver()

    yield driver

    driver.quit()

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    # driver.find_element().value_of_css_property('')
    driver.set_window_size(width=1000, height=1000)
    yield driver
    driver.quit()

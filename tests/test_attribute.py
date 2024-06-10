import pytest

from pages.text_box import TextBox
import allure


@allure.feature('check attr')
@allure.story('Проверка атрибута placeholder')
@allure.severity(allure.severity_level.NORMAL)
def test_placeholder(browser):
    text_box = TextBox(browser)

    text_box.visit()
    assert text_box.name.get_dom_attribute('placeholder') == 'Full Name'


@allure.feature('check attr')
@allure.story('Fail тест')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.skipif(True, )
def test_placeholder(browser):
    assert 111 == 222

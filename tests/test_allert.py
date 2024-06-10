import time

import allure

from pages.alerts import Alerts


@allure.title('Проверка видимости алерта')
def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert()
    alert_page.alert().accept()


@allure.title('Подтверждение и текст алерта')
def test_alert_text(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()


@allure.title('Отмена алерта')
def test_confirm(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.confirmButton.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.confirmResult.get_text() == "You selected Cancel"


@allure.title('Проверка ввода текста в алерт')
def test_prompt(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.promtButton.click()
    time.sleep(2)
    alert_page.alert().send_keys('Boris')
    alert_page.alert().accept()
    assert alert_page.promptResult.get_text() == 'You entered Boris'
    time.sleep(2)



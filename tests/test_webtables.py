import time
import allure
from pages.tables import Tables


@allure.title('Проверка блока No rows found')
def test_tables(browser):
    page_tables = Tables(browser)

    page_tables.visit()
    assert not page_tables.no_data.exist()

    ''' Удаляем все записи '''
    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()

    time.sleep(2)
    assert page_tables.no_data.exist()

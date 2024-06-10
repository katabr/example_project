from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self, driver):
        self.path_url = '/webtables'
        self.pageData = {
            'title': 'DEMOQA'
        }
        super().__init__(driver, self.path_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, '[title="Delete"]')


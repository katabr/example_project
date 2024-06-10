from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.path_url = '/modal-dialogs'
        self.pageData = {
            'title': 'DEMOQA'
        }
        super().__init__(driver, self.path_url)

        self.btn_sidebar_first_child = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, 'header > a > img')

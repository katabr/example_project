from pages.base_page import BasePage
from components.components import WebElement


class Alerts(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        self.pageData = {
            'title': 'DEMOQA'
        }
        super().__init__(driver, self.base_url)

        self.alertButton = WebElement(driver, '#alertButton')
        self.confirmButton = WebElement(driver, '#confirmButton')
        self.promtButton = WebElement(driver, '#promtButton')
        self.confirmResult = WebElement(driver, '#confirmResult')
        self.promptResult = WebElement(driver, '#promptResult')


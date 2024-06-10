from pages.base_page import BasePage
from components.components import WebElement


class Droppable(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/droppable'
        self.pageData = {
            'title': 'DEMOQA'
        }
        super().__init__(driver, self.base_url)

        self.drag = WebElement(driver, '#draggable')
        self.drop = WebElement(driver, '#droppable')
        self.box = WebElement(driver, '#droppableExample-tabpane-simple')

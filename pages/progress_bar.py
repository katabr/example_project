

from pages.base_page import BasePage
from components.components import WebElement


class Progress(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        self.pageData = {
            'title': 'DEMOQA'
        }
        super().__init__(driver, self.base_url)

        self.button = WebElement(driver, '#startStopButton')
        self.bar = WebElement(driver, '#progressBar > div')
        # self.restrictedY = WebElement(driver, '#restrictedY')
        # self.box = WebElement(driver, '#draggableExample-tab-axisRestriction')
        # self.box = WebElement(driver, '#droppableExample-tabpane-simple')

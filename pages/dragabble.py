from pages.base_page import BasePage
from components.components import WebElement


class Drag(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        self.pageData = {
            'title': 'DEMOQA'
        }
        super().__init__(driver, self.base_url)

        self.slider = WebElement(driver, '#sliderContainer > div.col-9 > span > input')
        self.inp = WebElement(driver, '#sliderValue')
        # self.restrictedY = WebElement(driver, '#restrictedY')
        # self.box = WebElement(driver, '#draggableExample-tab-axisRestriction')
        # self.box = WebElement(driver, '#droppableExample-tabpane-simple')

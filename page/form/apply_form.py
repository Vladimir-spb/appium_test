from element.button import Button
from element.text import Text
from page.base_page import BasePage
from utils.swipe_utils import SwipeUtils, SwipeDirection


class ApplyForm(BasePage):
    PAGE_NAME = 'Apply Form'
    UNIQ_ELEMENT = ('//*[@resource-id="ru.dns.shop.android:id/title_text"]', PAGE_NAME)

    DELETE_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/positive_button"]', 'Аксесуары и услуги')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__delete_button = Button(*self.DELETE_BUTTON)

    def click_delete(self):
        self.__delete_button.click_on_element()

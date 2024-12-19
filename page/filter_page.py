from element.button import Button
from page.base_page import BasePage
from utils.swipe_utils import SwipeUtils, SwipeDirection


class FilterPage(BasePage):
    PAGE_NAME = 'Filter Page'
    UNIQ_ELEMENT = ('//*[@resource-id="ru.dns.shop.android:id/toolbar"]//*[@text="Фильтры"]', PAGE_NAME)

    SIZE_FLASH_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/title_text" and @text="Объем (ГБ)"]', 'Объем (ГБ)')
    SIZE_128_GB = ('//*[@resource-id="ru.dns.shop.android:id/check" and contains(@text,"128 ГБ")]', 'Объем 128 (ГБ)')
    APPLY_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/apply_button"]', 'Применить')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__size_flash_button = Button(*self.SIZE_FLASH_BUTTON)
        self.__size_128_gb_button = Button(*self.SIZE_128_GB)
        self.__apply_button = Button(*self.APPLY_BUTTON)

    def swipe_from_size_flash_button(self):
        SwipeUtils.swipe_until_element_will_be_found_by_locator(
            self.__size_flash_button.get_locator(),
            SwipeDirection.UP
        )

    def click_size_flash_button(self):
        self.__size_flash_button.click_on_element()

    def click_size_128_gb_button(self):
        self.__size_128_gb_button.click_on_element()

    def click_apply_button(self):
        self.__apply_button.click_on_element()


filter_page = FilterPage()

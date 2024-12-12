from element.button import Button
from page.base_page import BasePage
from utils.swipe_utils import SwipeUtils, SwipeDirection


class CatalogPage(BasePage):
    PAGE_NAME = 'Catalog Page'
    UNIQ_ELEMENT = ('//*[@resource-id="ru.dns.shop.android:id/search_edit"]', PAGE_NAME)

    SEARCH_FIELD = ('//*[@resource-id="ru.dns.shop.android:id/search_edit"]', 'Поле поиска')
    ACCESSORIES_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/title_text" and @text="Аксессуары и услуги"]', 'Аксесуары и услуги')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__accessories_button = Button(*self.ACCESSORIES_BUTTON)

    def swipe_from_accessories_button(self):
        SwipeUtils.swipe_until_element_will_be_found_by_locator(
            self.__accessories_button.get_locator(),
            SwipeDirection.UP
        )

    def click_accessories_button(self):
        self.__accessories_button.click_on_element()


catalog_page = CatalogPage()

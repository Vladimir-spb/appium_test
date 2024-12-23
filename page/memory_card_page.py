from selenium.webdriver.common.by import By

from element.button import Button
from element.text import Text
from page.base_page import BasePage
from utils.screen_utils import ScreenshotUtils


class MemoryCardPage(BasePage):
    PAGE_NAME = 'Memory Card Page'
    UNIQ_ELEMENT = ('//*[@resource-id="ru.dns.shop.android:id/toolbar"]/child::*[@text="Карты памяти"]', PAGE_NAME)

    FILTER_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/filter_button"]', 'Фильтры')
    FIRST_ITEM = ('//*[@resource-id="ru.dns.shop.android:id/product_list"]/androidx.cardview.widget.CardView[1]/android.view.ViewGroup', 'Первый элемент')
    PRICE_ITEM = ('//*[@resource-id="ru.dns.shop.android:id/current_price_text"]','Цена продукта')
    NAME_ITEM = ('//*[@resource-id="ru.dns.shop.android:id/product_title_text"]','Название продукта')

    BUY_BUTTON = ('(//*[@resource-id="ru.dns.shop.android:id/buy_button"])[1]','Button_buy')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__filter_button = Button(*self.FILTER_BUTTON)
        self.__first_item = Text(*self.FIRST_ITEM)
        self.__price_item = Text(*self.PRICE_ITEM)
        self.__name_item = Text(*self.NAME_ITEM)
        self.__buy_button = Button(*self.BUY_BUTTON)

    def click_filter_button(self):
        self.__filter_button.click_on_element()

    def __get_first_item(self):
        return self.__first_item.find_element()

    def get_price(self):
        elem = self.__get_first_item()
        return elem.find_element(By.XPATH, self.__price_item.get_locator()).text

    def get_name_item(self):
        elem = self.__get_first_item()
        return elem.find_element(By.XPATH, self.__name_item.get_locator()).text

    def open_page_item(self):
        elem = self.__get_first_item()
        elem.find_element(By.XPATH, self.__name_item.get_locator()).click()

    def get_screenshot_buy_button(self):
        path = ScreenshotUtils.take_element_screenshot(self.__buy_button)
        return path


memory_card_page = MemoryCardPage()

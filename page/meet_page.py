from element.button import Button
from element.text import Text
from page.base_page import BasePage


class MeetPage(BasePage):
    PAGE_NAME = 'Meet Page'
    UNIQ_ELEMENT = ('//*[@resource-id="ru.dns.shop.android:id/empty_content_details_text"]', PAGE_NAME)
    CHANGE_CITY_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/change_current_settlement_button"]', 'Кнопка смены города')
    OK_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/confirm_current_settlement_button"]', 'Кнопка "Все верно"')
    CITY_NAME = ('//*[@resource-id="ru.dns.shop.android:id/current_settlement_text"]', 'Название города')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__change_city_button = Button(*self.CHANGE_CITY_BUTTON)
        self.__ok_button = Button(*self.OK_BUTTON)
        self.__city_name = Text(*self.CITY_NAME)

    def click_change_city_button(self):
        self.__change_city_button.click_on_element()

    def click_ok_button(self):
        self.__ok_button.click_on_element()

    def get_name_city(self):
        return self.__city_name.get_text_from_element()


meet_page = MeetPage()

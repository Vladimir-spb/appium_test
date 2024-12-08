from element.button import Button
from element.text import Text
from page.base_page import BasePage


class MeetPage(BasePage):
    PAGE_NAME = 'Meet Page'
    UNIQ_ELEMENT = ('//*[contains(@resource-id,"ru.dns.shop.android:id/empty_content_details_text")]', PAGE_NAME)
    CHANGE_CITY_BUTTON = ('//*[contains(@text,"Сменить город")]', 'Кнопка смены города')
    OK_BUTTON = ('//*[contains(@text,"Все верно")]', 'Кнопка "Все верно"')
    CITY_NAME = ('//*[contains(@text,"Ваш город")]/following-sibling::android.widget.TextView', 'Название города')

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

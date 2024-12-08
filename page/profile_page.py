from element.button import Button
from element.text import Text
from page.base_page import BasePage


class ProfilePage(BasePage):
    PAGE_NAME = 'Profile Page'
    UNIQ_ELEMENT = ('//android.widget.TextView[@text="Профиль"]', PAGE_NAME)

    LOGIN_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/login_button"]', 'Кнопка войти')
    CITY_NAME = ('//*[@resource-id="ru.dns.shop.android:id/settlement_text"]', 'Город')
    FAVOURITES_BUTTON = ('//*[contains(@text,"Избранное")]', 'Избранное')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__city_name = Text(*self.CITY_NAME)
        self.__login_button = Button(*self.LOGIN_BUTTON)
        self.__favourites_button = Button(*self.FAVOURITES_BUTTON)

    def is_login_button_on_display(self):
        return self.__login_button.check_element_on_display()

    def get_city_name(self):
        return self.__city_name.get_text_from_element()

    def click_favourites_button(self):
        self.__favourites_button.click_on_element()


profile_page = ProfilePage()

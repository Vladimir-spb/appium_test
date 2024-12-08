from element.button import Button
from element.text import Text
from page.base_page import BasePage
from page.form.location_form import LocationForm


class ChangeCityPage(BasePage):
    PAGE_NAME = 'Change City Page'
    UNIQ_ELEMENT = ('//*[contains(@text,"Ваш город")]', PAGE_NAME)
    INPUT_FIELD = ('//*[@resource-id="ru.dns.shop.android:id/search_edit"]', 'Поле ввода')

    CITY_NAME = '//*[@resource-id="ru.dns.shop.android:id/settlement_name_text" and contains(@text,"{}")]'

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__input_field = Text(*self.INPUT_FIELD)
        self.location_form = LocationForm()

    def input_city_name(self, name_city):
        self.__input_field.send_keys(name_city)

    def click_city(self, name_city):
        Button(self.CITY_NAME.format(name_city), f"Город {name_city}").click_on_element()


change_city_page = ChangeCityPage()

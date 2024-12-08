from element.button import Button
from page.base_page import BasePage


class UpdateForm(BasePage):
    PAGE_NAME = 'Update Form'
    UNIQ_ELEMENT = ('//*[contains(@content-desc, "Доступно обновление")]', PAGE_NAME)
    CLOSE_BUTTON = ('//*[contains(@content-desc,"Закрыть диалоговое окно")]', 'Кнопка "Закрыть"')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__close_button = Button(*self.CLOSE_BUTTON)

    def close_update(self):
        self.__close_button.click_on_element()

from element.base_element import BaseElementClass
import logging

logger = logging.getLogger("Input Element")


class InputElement(BaseElementClass):
    def __init__(self, loc, name_of):
        super().__init__(loc, name_of)

    def input_text(self, text):
        try:
            logger.info(f'ввод текста в элемент {self.get_name()}')
            self.find_element().send_keys(text)
        except Exception as e:
            logger.error(f'все рухнуло когда пытались ввести текст в элемент {self.get_name()}, '
                         f'подробности смотри {e}')

from element.base_element import BaseElementClass
import logging

logger = logging.getLogger("Button")


class Button(BaseElementClass):
    def __init__(self, loc, name_of):
        super().__init__(loc, name_of)

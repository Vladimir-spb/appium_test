import logging

from element.base_element import BaseElementClass

logger = logging.getLogger("Uniq Element")


class UniqElement(BaseElementClass):
    def __init__(self, loc, name_of):
        super().__init__(loc, name_of)

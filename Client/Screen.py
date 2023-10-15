from Button import *
from typing import List

class Screen:
    def __init__(self, background_image_name: str, buttons: List[Button]):
        self.active = False
        self.background_image = background_image_name + ".gif"
        self.buttons = buttons

    def display(self) -> None:
        window.bgpic(self.background_image)
        for button in self.buttons:
            button.display()
        self.active = True

    def hide(self) -> None:
        self.active = False
        for button in self.buttons:
            button.hide()
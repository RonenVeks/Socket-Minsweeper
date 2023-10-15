from Window import *
from PIL import Image
from time import sleep

class Button(ClickableObject):
    def __init__(self, x: int, y: int, image_name: str):
        self.turtle = Turtle()
        setup_turtle(self.turtle)
        self.function = None

        self.image = image_name + ".gif"
        self.animation_image = image_name + "_animation.gif"
        window.addshape(self.image)
        window.addshape(self.animation_image)
        self.turtle.shape(self.image)

        width, height = Image.open(self.image).size
        super().__init__(x, y, width, height)

        self.turtle.goto(x, y)

    def display(self) -> None:
        self.turtle.st()
        self.clickable = True

    def hide(self) -> None:
        self.clickable = False
        self.turtle.ht()
    
    def clicked(self) -> None:
        self.clickable = False
        self.turtle.shape(self.animation_image)
        sleep(0.1)
        self.turtle.ht()
        self.function()
from turtle import Screen, Turtle, mainloop
from abc import ABC

window = Screen();
window.setup(1000, 1000)
window.bgcolor('black')
window.title('Minesweeper')

def setup_turtle(t: Turtle) -> None:
    t.pu()
    t.ht()
    t.speed(0)

class ClickableObject(ABC):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.clickable = False
        self.x = x
        self.y = y
        self.min_x = x - (width / 2)
        self.max_x = x + (width / 2)
        self.min_y = y - (height / 2)
        self.max_y = y + (height / 2)

    def click_check(self, x, y) -> bool:
        return x >= self.min_x and x <= self.max_x and y >= self.min_y and y < self.max_y and self.clickable
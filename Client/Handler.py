from Screen import *

class ButtonsHandler:
    #Starting screen
    start_button = Button(0, -100, "StartButton")
    exit_button = Button(0, -250, "ExitButton")

    #Board Size Selection Screen
    size_9x9_button = Button(0,100, "9x9BoardSize")
    size_16x16_button = Button(0, -50, "16x16BoardSize")
    size_25x25_button = Button(0, -200, "25x25BoardSize")

class ScreensHandler:
    start_screen = Screen("StartScreenBackground", [ButtonsHandler.start_button, ButtonsHandler.exit_button])
    board_size_selection_screen = Screen("SizeScreenBackground", [ButtonsHandler.size_9x9_button, ButtonsHandler.size_16x16_button, ButtonsHandler.size_25x25_button])
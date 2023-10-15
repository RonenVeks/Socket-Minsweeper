from Handler import ScreensHandler, Screen, ButtonsHandler
from Window import window
from turtle import mainloop
import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 7783 #ascii values of M (77) and S (83)

current_screen = ScreensHandler.start_screen
sock = socket.socket()

def change_screens(next_screen: Screen) -> None:
    global current_screen
    current_screen.hide()
    current_screen = next_screen
    current_screen.display()

def f_start_button() -> None:
    global sock
    server_address = (SERVER_IP, SERVER_PORT)
    try:
        sock.connect(server_address)
    except Exception:
        print("Failed connecting to server")
        exit()
    print("connected")
    change_screens(ScreensHandler.board_size_selection_screen)

def f_exit_button() -> None:
    exit()

def f_size_9x9_button() -> None:
    global sock
    print("bingalabingbangbingbangbong")

    msg = 'size 9x9'
    sock.sendall(msg.encode())

def initialize_button_functions():
    ButtonsHandler.start_button.function = f_start_button
    ButtonsHandler.exit_button.function = f_exit_button
    ButtonsHandler.size_9x9_button.fucntion = f_size_9x9_button

def main() -> None:
    global current_screen

    initialize_button_functions()
    current_screen.display()

if __name__ == '__main__':
    main()

def click(x: int, y: int) -> None:
    global current_screen
    for button in current_screen.buttons:
        if button.click_check(x, y): button.clicked()

window.onclick(click)

mainloop()

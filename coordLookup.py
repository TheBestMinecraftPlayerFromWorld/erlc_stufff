from pynput.mouse import Listener
import pynput

def on_click(x, y, button, pressed):
    print(button)
    if pressed:
        print('Mouse button pressed at ({}, {})'.format(x, y))
    else:
        print('Mouse button released at ({}, {})')
    if button == pynput.mouse.Button.middle:
        exit()

# Set up the listener
with Listener(on_click=on_click) as listener:
    listener.join()

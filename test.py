import pyautogui
import keyboard

def getPixel(screen,x,y):
    # Get the RGB value of a specific pixel
    r, g, b = screen.getpixel((x, y))

    # Check the green component
    return (r,g,b)

while not keyboard.is_pressed("j"):
    screen = pyautogui.screenshot()
    print(getPixel(screen,pyautogui.position().x,pyautogui.position().y))
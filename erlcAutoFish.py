import pyautogui
from PIL import Image
import time
import win32api, win32con
import random as rd
import mouse
import keyboard
# Take a screenshot

def getPixel(screen,x,y):
    # Get the RGB value of a specific pixel
    r, g, b = screen.getpixel((x, y))

    # Check the green component
    return (r,g,b)
def slRd(st=1,en=5,z=100):
    time.sleep(rd.randint(st,en)/z)
lastWhiteN = 1
casts = 0
lastTime = time.time()
keyboard.wait("k")
while not (casts>=500 or keyboard.is_pressed("J")):
    screenshot = pyautogui.screenshot()
    mostlyGreenY = 0
    mostlyGreenG = 0
    whiteY = 0
    whiteN = 0
    for y in range(380,700):
        pixel = getPixel(screenshot,1700,y)
        if (pixel[0] == pixel[1] == pixel[2]) and pixel[0] >= 200:
            whiteY+=y
            whiteN+=1
        elif pixel[1] > mostlyGreenG:
            mostlyGreenG = pixel[1]
            mostlyGreenY = y
    
    if whiteN!=0:    
        whiteY = whiteY // whiteN
        if whiteY>mostlyGreenY:
            mouse.click("left")
            slRd(z=100)
            mouse.release("left")
            slRd(z=100)
    elif whiteN != lastWhiteN:
        keyboard.press_and_release("1")
        slRd(z=10)
        keyboard.press_and_release("3")
        slRd(z=10)
        keyboard.press("s")
        slRd(6,6,z=15)
        keyboard.release("s")
        slRd(z=10)
        keyboard.press("w")
        slRd(2,2,z=15)
        keyboard.release("w")
        slRd(z=10)
        mouse.click("left")
        slRd(z=100)
        mouse.release("left")
        slRd(z=100)
        casts+=1
        lastTime = time.time()
        print(casts,"casts - \"J\" to stop")
    
    if time.time() > lastTime + 5 and whiteN==0:
        mouse.click("left")
        slRd(z=100)
        mouse.release("left")
        slRd(z=10)
        lastTime = time.time()

    lastWhiteN = whiteN
        

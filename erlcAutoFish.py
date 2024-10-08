import pyautogui
import PIL
import time
import random as rd
import mouse
import keyboard
import base64
import io
import requests
import math

def getPixel(screen,x,y):
    # Get the RGB value of a specific pixel
    r, g, b = screen.getpixel((x, y))

    # Check the green component
    return (r,g,b)
def slRd(st=1,en=5,z=100):
    time.sleep(rd.randint(st,en)/z)
def getPngURL(image):
    # Convert image to bytes
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    # Encode bytes to base64
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')

    # Create data URL
    data_url = f"data:image/png;base64,{img_base64}"

    return data_url
def ocr(imgUrl):
    pass
lastWhiteN = 1
casts = 0
lastTime = time.time()
keyboard.wait("k")
total = 50000
while not (casts>=total or keyboard.is_pressed("J")):
    screenshot = pyautogui.screenshot()
    mostlyGreenY = 0
    mostlyGreenG = 0
    whiteY = 0
    whiteN = 0
    x = round((1700/1920)*screenshot.size[0])
    ly = 0
    for y in range(math.floor((380/1080)*screenshot.size[1]),math.ceil((700/1080)*screenshot.size[1])):
        ry = round(y)
        if ry == ly:
            continue
        pixel = getPixel(screenshot,x,ry)
        if (pixel[0] == pixel[1] == pixel[2]) and pixel[0] >= 200:
            whiteY+=ry
            whiteN+=1
        elif pixel[1] > mostlyGreenG:
            mostlyGreenG = pixel[1]
            mostlyGreenY = ry
        ly = y
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
        #keyboard.press("s")
        #slRd(4,4,z=15)
        #keyboard.release("s")
        
        """slRd(z=10)
        keyboard.press("w")
        slRd(8,8,z=15)
        keyboard.release("w")"""
        slRd(z=10)
        mouse.click("left")
        slRd(z=100)
        mouse.release("left")
        slRd(z=100)
        casts+=1
        lastTime = time.time()
        print(casts,"casts - \"J\" to stop. Otherwise:",total-casts,"left")
        #screenshot.crop((545,1095,1497,1181))
        #ocr(getPngURL(screenshot))
    
    if time.time() > lastTime + 5 and whiteN==0:
        mouse.click("left")
        slRd(z=100)
        mouse.release("left")
        slRd(z=10)
        lastTime = time.time()

    lastWhiteN = whiteN
        

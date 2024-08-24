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

pins = 6
midX_PointRatio = .5
YLY_PointRatio  = .5
YLY_Offset      = -3



keyboard.wait("k") # Wait to be in menu

sz = pyautogui.screenshot().size
midX_Point = round(sz[0]*midX_PointRatio)
YLY_Point  = round(sz[1]*YLY_PointRatio + YLY_Offset)

mostLeftX_Point = 300#pyautogui.position().x
currentPoint_X  = mostLeftX_Point
xPerPin         = 30+60#abs((mostLeftX_Point - midX_Point) // 3)
pin = 0
done = False

def is_about_same(a,b,ra):
    return abs(a-b) <=ra

while not (keyboard.is_pressed("j") or done):
    screen = pyautogui.screenshot()
    print(currentPoint_X,YLY_Point)
    px = getPixel(screen,currentPoint_X,YLY_Point)
    print(px,"\n-------")    
    if is_about_same(px[0],px[1],5) and is_about_same(px[1],px[2],5) and px[0] >= 70:
        slRd(z=500)
        mouse.click("left")
        slRd(z=100)
        mouse.release("left")
        slRd(z=100)
        print(pin,mostLeftX_Point,xPerPin,currentPoint_X)
        currentPoint_X+=xPerPin
        pin+=1
        slRd(z=15)
    if pin>=pins:
        done = True

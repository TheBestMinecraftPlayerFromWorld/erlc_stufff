import pyautogui
import keyboard

def on_key_event(event):
    if event.name == 't':  # Change 'a' to the key you want to detect
        move_and_click()

def move_and_click():
    pyautogui.moveTo(100, 305,0.01)  # Change to your desired coordinates
    pyautogui.click()

# Listen for the key press
keyboard.on_press(on_key_event)

# Keep the script running
keyboard.wait('esc')  # Change 'esc' to the key you want to use to stop the script

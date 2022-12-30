"""
draw_square.py
    Capabilities:
        Will draw a square using paint tool

    Limitation:
        Can't open the paint. The paint must be open and the author will change window
"""

import pyautogui
import time

# Give python file some time to before continuing
time.sleep(3)

# Mouse Up and Down Example on Paint:
pyautogui.mouseDown(300, 400, button='left')  # Horizontal Line (left to right)
pyautogui.moveTo(800, 400, 2)
pyautogui.mouseUp()

pyautogui.mouseDown(800, 400, button='left')  # Vertical Line (right to down)
pyautogui.moveTo(800, 800, 2)
pyautogui.mouseUp()

pyautogui.mouseDown(800, 800, button='left')  # Horizontal Line (down to left)
pyautogui.moveTo(300, 800, 2)
pyautogui.mouseUp()

pyautogui.mouseDown(300, 800, button='left')  # Vertical Line (left to up)
pyautogui.moveTo(300, 400, 2)
pyautogui.mouseUp()

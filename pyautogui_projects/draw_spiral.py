"""
draw_spiral.py
    Capabilities:
        Will draw a spiral in paint
"""

import pyautogui
import time

time.sleep(1)
distance = 300

# The spiral should stop at the center
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button='left')
    distance = distance - 40
    pyautogui.dragRel(0, distance, 1, button='left')
    pyautogui.dragRel(-distance, 0, 1, button='left')
    distance = distance - 50
    pyautogui.dragRel(0, -distance, 1, button='left')
time.sleep(2)
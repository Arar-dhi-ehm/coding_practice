"""
tiktok_liker.py
    like and scroll down then like again
"""

import pyautogui
import time

# Always check the coordinates first, by using pyautogui.position()
# print(pyautogui.position())  # prints cursor coordinates

time.sleep(3)
# range will be the number of TikTok's you want to like
for i in range(10):
    pyautogui.moveTo(450, 500)  # video center
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.moveTo(845, 515)  # toggle button for up and down
    time.sleep(1)
    pyautogui.leftClick()
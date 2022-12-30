"""
keyboard_function.py
    Capabilities:
        Open website by keyboard typing
        Scroll down
        Click a link
        Highlight text
        Copy text
        Open an app through windows search bar
        Paste text
"""

import pyautogui
import time

time.sleep(2)
pyautogui.click(608, 57, 3)
time.sleep(2)
pyautogui.typewrite('wikipedia')
time.sleep(1)
pyautogui.press('enter')

# Scrollbar down
time.sleep(2)
pyautogui.moveTo(1910, 203)
pyautogui.scroll(-5000)

# Click Privacy Policy
time.sleep(2)
pyautogui.click(1207, 716, 3)

# Highlight a paragraph
time.sleep(2)
pyautogui.mouseDown(80, 318, button='left')
pyautogui.moveTo(334, 540, 2)
pyautogui.mouseUp()

# Copy the paragraph
pyautogui.hotkey('ctrl', 'c')

# Click search in windows and type notepad; press enter
time.sleep(2)
pyautogui.click(94, 1057, 3)
pyautogui.typewrite('notepad')
pyautogui.press('enter')

# open notepad and paste
time.sleep(2)
pyautogui.click(1053, 307, 3)
pyautogui.hotkey('ctrl', 'v')
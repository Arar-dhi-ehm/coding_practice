"""
wikipedia_search.py
    - Control keyboard and mouse using pyautogui

    Capabilities:

    Limitations:

    Notes:
        Instructions:
            - Use Firefox
                Point(x=796, y=1059, duration=2)
            - Open 'https://www.wikipedia.org/'
            - Click English Articles
                Point(x=782, y=294)
            - Scrollbar slide down
                move to x coordinate:
                        Point(x=1905, y=249)
                drag scrollbar from move:
                        Point(x=1910, y=870)
            - Click Wiktionary
                Point(x=1579, y=454)

"""

import pyautogui
import time

# Get the x,y coordinate of your cursor
time.sleep(3)  # After 3 secs it will print the coordinate of your mouse
# print(pyautogui.position())

# Move the mouse to the location of Firefox browser
pyautogui.moveTo(796, 1059, 1)

# After moving the mouse use leftClick, rightClick, doubleClick, tripleClick
pyautogui.leftClick()
time.sleep(5)

# Type in the browser
pyautogui.typewrite('www.wikipedia.org')
time.sleep(5)
pyautogui.press('enter')
time.sleep(3)

# Click English hyperlink
pyautogui.moveTo(782, 294, 1)
pyautogui.leftClick()


# Hold and drag the scrollbar to go down
pyautogui.moveTo(1905, 249, 1)
pyautogui.dragTo(1910, 870, 2, button='left')
time.sleep(2)

# Scroll down 5 "clicks"
# pyautogui.moveTo(1905, 249, 1)
# time.sleep(1)
# pyautogui.leftClick()
# pyautogui.scroll(-500)
# pyautogui.scroll(-500)
# time.sleep(2)

# Click 'Wiktionary'
pyautogui.moveTo(1579, 454, 1)
pyautogui.leftClick()

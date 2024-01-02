import time

import pyautogui


def prep101Next():
    pyautogui.press("right")


def stuDocUNext():
    pyautogui.moveTo(392, 753)
    time.sleep(0.2)
    pyautogui.click()
    pyautogui.moveTo(200, 753)
    time.sleep(4)

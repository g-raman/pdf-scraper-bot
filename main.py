import os
import time

import pyautogui

import png_merger
from clean_up import clean_up
from next_methods import prep101Next

regions = {"prep101": (675, 70, 1180, 1520), "stuDocU": (820, 420, 890, 1150)}
defaultDir = "images"
defaultPath = f"./{defaultDir}/"


def main():
    totalPages = int(input("How many total pages: "))
    startPage = int(input("What page are you starting on: "))
    outputFile = input("Enter the name of the output file: ")

    if not os.path.isdir(defaultDir):
        os.mkdir(defaultDir)

    time.sleep(3)
    pageCount = totalPages - startPage + 1
    for i in range(0, pageCount):
        screenshot = pyautogui.screenshot(region=regions["prep101"])
        screenshot.save(f"{defaultPath}page_{i}.png")
        prep101Next()

    png_merger.convert_to_pdf(outputFile, defaultPath, pageCount)
    clean_up(defaultPath, defaultDir)


if __name__ == "__main__":
    main()

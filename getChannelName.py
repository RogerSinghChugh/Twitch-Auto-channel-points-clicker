from datetime import datetime as dt
import pygetwindow as gw
import pytesseract
import pyautogui
import time
import re


chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Roger\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

x = chrome_window.left
y = chrome_window.top
width = chrome_window.width
height = chrome_window.height

# Print the coordinates
# print(f"Chrome window coordinates: x={x}, y={y}, width={width}, height={height}")


def get_channel_name():
    time.sleep(1)
    screenshot = pyautogui.screenshot(region=(x+100, y+50, width-450, height - 985))
    #screenshot.show()
    channel_name = pytesseract.image_to_string(screenshot).strip()
    try:
        result = re.search(r"/(.*)", channel_name).group(1)
        if result:
            return result
        else:
            return 'NotFound'
    except Exception as e:
        print(f"Exception: {e} at {dt.now()}")
        return 'NotFound'
import numpy as np
import pyautogui
import cv2
import pytesseract
import time

time.sleep(2)


def SB(x1, y1, x2, y2):

    screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    image = np.array(screenshot)


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


    detected_text = pytesseract.image_to_string(thresholded, config='--psm 6 digits')


    try:
        result = int(detected_text)
    except ValueError:
        result = 0

    print("下载中数量:", result)
    return result


def CL():  
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shiftright')
    pyautogui.keyDown('shiftleft')
    pyautogui.press('down', presses=100)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shiftright')
    pyautogui.keyUp('shiftleft')
    
    time.sleep(3)
    

    pyautogui.hotkey('alt')
    pyautogui.hotkey('r')

    pyautogui.press('down', presses=7)

    pyautogui.press('right')

    pyautogui.press('enter')
    
    pyautogui.press('down')    
    print("√添加100个")


while True:

    result = SB(204, 345, 235, 368)

    if result < 100:    
        print("小于100")
        CL()
        print("---------------")
    else:
        print("大于100")
        print("")
        print("---------------")


    time.sleep(5)

CL()

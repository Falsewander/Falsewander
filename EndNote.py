import numpy as np
import pyautogui
import cv2
import pytesseract
import time

# 等待两秒
time.sleep(2)

# 设置 Tesseract-OCR 的安装路径
# pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

# 识别区域内的数字
def SB(x1, y1, x2, y2):
    # 从屏幕上截取指定区域的图像
    screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    image = np.array(screenshot)

    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用适当的图像处理技术（这里使用简单的阈值化）来准备图像进行文本识别
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 使用 Tesseract-OCR 来识别图像中的数字
    detected_text = pytesseract.image_to_string(thresholded, config='--psm 6 digits')

    # 将识别的文本转换为整数
    try:
        result = int(detected_text)
    except ValueError:
        result = 0  # 如果无法转换为整数，则将结果设为0

    # 返回识别结果
    print("下载中数量:", result)
    return result


# 定义函数，模拟按键操作
def CL():  
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shiftright')
    pyautogui.keyDown('shiftleft')
    pyautogui.press('down', presses=100)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shiftright')
    pyautogui.keyUp('shiftleft')
    
    time.sleep(3)
    
    # 按下Alt+R
    pyautogui.hotkey('alt')
    pyautogui.hotkey('r')
    # 等待半秒

    # 按下下键7次
    pyautogui.press('down', presses=7)

    # 按下右箭头键
    pyautogui.press('right')

    # 按下回车键
    pyautogui.press('enter')
    
    pyautogui.press('down')    
    print("√添加100个")


# 无限循环
while True:
    # 调用SB函数获取返回值
    result = SB(204, 345, 235, 368)
#   result = SB(260, 345, 300, 367)
    # 根据返回值判断输出消息
    if result < 100:    
        print("小于100")
        CL()
        print("---------------")
    else:
        print("大于100")
        print("")
        print("---------------")

    # 休眠1秒
    time.sleep(5)

CL()

import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import keyboard
from time import sleep
import asyncio

k = True

 
def capture_telegram_window():
    # Захоплення зображення екрану
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    # Перетворення зображення в формат OpenCV
    frame = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    return frame

def find_green_and_click(frame):
    lower_green = np.array([40, 80, 80])
    upper_green = np.array([80, 255, 255])

    # Перетворення зображення з BGR в HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Маска для зеленого кольору
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Знаходження контурів
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Ігнорування маленьких областей
        if cv2.contourArea(contour) < 500:
            continue
        # Знаходження координат для кліку
        x, y, w, h = cv2.boundingRect(contour)
        center_x = x + w // 2
        center_y = y + h // 2

        # Виконання кліку мишкою
        pyautogui.click(center_x, center_y)
        break

# async def interrupt():
#     global k
#     while k:
#         # Перевірка на натискання клавіші 'Space'
#         if keyboard.is_pressed('space'):
#             print("Цикл перервано.")
#             k = False
#         await asyncio.sleep(0.1)  # Додано затримку, щоб знизити навантаження на процесор

# # Виклик асинхронної функції
# asyncio.run(interrupt())

print('Start')
for i in range(1,4):
    sleep(1)
    print(i)
while k:
     frame = capture_telegram_window()
     find_green_and_click(frame) 
            
    # Затримка для уникнення надто швидкого виконання циклу
    #  pyautogui.sleep(1)

    

   
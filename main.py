import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture
from vision import Vision
import keyboard
import winsound
import pyautogui
import win32gui
import asyncio
import threading

def lclick(x, y, times):
        i=0
        for i in range (1):
            pyautogui.click(x, y)
async def click(trash):
    
    while(True):
        pyautogui.moveTo(0, 0)
        screenshot = await wincap.get_screenshot()
        
        points = vision_limestone.find(screenshot, trash)   
        for point in points:
            pyautogui.click(point[0], point[1])
        if keyboard.is_pressed('q'):  
            winsound.Beep(400, 100)
            break
        if keyboard.is_pressed("+"):
            if trash < 1:
                trash = trash + 0.01
                print(trash)
        if keyboard.is_pressed("-"):
            if trash > 0:
                trash = trash - 0.01
                print(trash)
        #time.sleep(0.1)
    await wait(trash)
    print('Done.')

async def wait(trash):
    while(True):
        if keyboard.is_pressed('c'):  
            winsound.Beep(500, 100)
            break
        if keyboard.is_pressed('x'):
            winsound.Beep(100, 300)
            exit()
    await click(trash)
pyautogui.FAILSAFE = False

print(win32gui.GetWindowText(525974))
wincap = WindowCapture()
vision_limestone = Vision('./data')
WindowCapture.list_window_names()

asyncio.run(wait(0.99))




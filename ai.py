from PIL import ImageGrab , ImageOps
import pyautogui 
from numpy import *
import time

class Cordinates():
    replaybtn = (685,370)
    dinosour = (441,371)

def restartgame():
    pyautogui.click(Cordinates.replaybtn)
    pyautogui.keyDown('down')


def pressSapce():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('jump')
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    box  = (Cordinates.dinosour[0]+70,Cordinates.dinosour[1],Cordinates.dinosour[0]+110,Cordinates.dinosour[1]+30)
    image = ImageGrab.grab(box) 
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
  
    return a.sum()


time.sleep(2)
restartgame()
time.sleep(1)

while True:
    found = imageGrab()
    if found != 1447:
        pressSapce()
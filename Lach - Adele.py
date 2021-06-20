import pyautogui as pg
import random
import decimal
import keyboard


pg.sleep(3)

def damage(times):
    for i in range(1,times+1):
        pg.mouseDown(x = 870, y = 155)
        pg.sleep(0.5)
        pg.mouseUp(x = 870, y = 155)
    
    pg.sleep(0.5)

def jumpup():
    keyboard.press_and_release('alt')
    pg.mouseDown(x = 1092, y = 255)
    pg.sleep(0.1)
    keyboard.press_and_release('alt')
    keyboard.press_and_release('alt')
    pg.sleep(0.3)
    pg.mouseUp(x = 1092, y = 255) 
    
    pg.sleep(0.5)

def jumpdown():
    
    pg.mouseDown(x = 1092, y = 300)
    keyboard.press_and_release('alt')
    pg.sleep(0.3)
    pg.mouseUp(x = 1092, y = 300)

    pg.sleep(0.5)
    
while True:
    for i in range(1,5):
        damage(times = 2)
        jumpup()
    keyboard.press_and_release('shift')
    for i in range(1,5):
        damage(times = 2)
        jumpdown()
    keyboard.press_and_release('shift')


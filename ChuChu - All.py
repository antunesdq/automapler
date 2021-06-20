import pyautogui as pg

pg.sleep(3)
while True:
    pg.mouseDown(x = 875, y = 155)
    pg.sleep(20)
    pg.mouseUp(x = 870, y = 155)
    pg.sleep(0.5)

    pg.click(x = 883, y = 300)
    pg.sleep(0.1)
    pg.doubleClick(x = 1092, y = 255)

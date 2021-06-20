import pyautogui as pg
import random
import decimal
pg.sleep(3)

while True:
    for i in range(1, random.randint(5,15)):
        
        pg.mouseDown(x = 870, y = 155)
        pg.sleep(float(decimal.Decimal(random.randrange(50,75)))/100)
        pg.mouseUp(x = 870, y = 155)
        
        pg.sleep(float(decimal.Decimal(random.randrange(50,150)))/100)
        
        pg.mouseDown(x = 845, y = 155)
        pg.sleep(float(decimal.Decimal(random.randrange(50,75)))/100)
        pg.mouseUp(x = 845, y = 155)

        pg.sleep(float(decimal.Decimal(random.randrange(50,150)))/100)

    pg.click(x = 883, y = 300)
    pg.sleep(float(decimal.Decimal(random.randrange(10,20)))/100)
    pg.doubleClick(x = 1092, y = 255)

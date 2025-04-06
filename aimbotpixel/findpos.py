import pyautogui as pg
import time as t

key = r'C:\Users\460226\Desktop\coding\pyautoguitest\aimbot\key.png'

while True:
    try:
        find = pg.locateOnScreen(key)
        if find:
            x,y,width,height = find
            print(x,y,width,height)
    except pg.ImageNotFoundException:
        print('nothing')
    t.sleep(0.5)
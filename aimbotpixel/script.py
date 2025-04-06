#352 141 1299 525
import pyautogui as pg
import keyboard as k
import time as t

run = False

def switch():
    global run
    run = not run
    if run:
        print('running')
    else:
        print('stopped')
k.add_hotkey('p',switch)

#rgb (149, 195, 232)
while True:
    area = pg.screenshot(region=(352,200,1299,525))
    width,height = area.size
    done = False
    if run:
        for x in range(0,width,5):
            if done:
                break
            for y in range(0,height,5):
                r,g,b = area.getpixel((x,y))
                if 145 <= r <= 153 and 191 <= g <= 199:
                    pg.click(x+380,y+200)
                    t.sleep(0.05)
                    done = True
                    break
    else:
        pass
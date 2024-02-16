import pyautogui as pg
import time
time.sleep(3)
for i in range(1,4):
    pg.typewrite("Thank you very much", interval=0)
    pg.press("Enter")

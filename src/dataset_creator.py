import pygetwindow as pw
from PIL import ImageGrab
import time
import ctypes
import os
import cv2

FPS = 0.3
APP_NAME = "Minecraft 1.7.10"
SAVE_FOLDER = "raw_dataset/"
FILE_INDEX = 0
t = 1 / FPS
running = True

if(not(os.path.exists(SAVE_FOLDER))):
    os.mkdir(SAVE_FOLDER)


def get_scaling_factor():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    dpi = user32.GetDpiForSystem()
    return dpi / 96


current_window = pw.getWindowsWithTitle(APP_NAME)[0]
left, top, right, bottom = current_window.left, current_window.top, current_window.right, current_window.bottom
factor = get_scaling_factor()

while(running):

    img = ImageGrab.grab()
    croped_img = img.crop((left * factor, top * factor, right * factor, bottom * factor))
    img_path = SAVE_FOLDER + "/" + str(FILE_INDEX) + ".jpg"
    croped_img.save(img_path)
    FILE_INDEX += 1
    time.sleep(t)

    key = cv2.waitKey(0)

    if (key == ord("l")):
        running = False
        break
    else:
        continue

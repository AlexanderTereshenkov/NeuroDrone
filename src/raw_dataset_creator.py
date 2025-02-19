from PIL import ImageGrab
import time
import os

FPS = 5
SAVE_FOLDER = "datasets/raw_dataset/"
FILE_INDEX = 362
t = 1 / FPS
running = True

if(not(os.path.exists(SAVE_FOLDER))):
    os.mkdir(SAVE_FOLDER)

while(running):
    img = ImageGrab.grab()
    img_path = SAVE_FOLDER + "/" + str(FILE_INDEX) + ".jpg"
    img.save(img_path)
    FILE_INDEX += 1
    time.sleep(t)

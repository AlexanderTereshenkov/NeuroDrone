
import os
import shutil
import math

RAW_YOLO_DATASET_FOLDER_PATH = "datasets/dataset"
PREPARED_DATASET_FOLDER_PATH = "datasets/pig_dataset"
#value from 0 to 1
train_val_percent = 0.75

if not(os.path.exists(PREPARED_DATASET_FOLDER_PATH + "/")):
    os.makedirs(PREPARED_DATASET_FOLDER_PATH + "/train/images/")
    os.makedirs(PREPARED_DATASET_FOLDER_PATH + "/train/labels/")

    os.makedirs(PREPARED_DATASET_FOLDER_PATH + "/val/images/")
    os.makedirs(PREPARED_DATASET_FOLDER_PATH + "/val/labels/")

all_images = os.listdir(RAW_YOLO_DATASET_FOLDER_PATH + "/images")
all_lables = os.listdir(RAW_YOLO_DATASET_FOLDER_PATH + "/labels")

cut_index = math.floor(len(all_images) * train_val_percent)

src_img = RAW_YOLO_DATASET_FOLDER_PATH + "/images/"
dst_img = PREPARED_DATASET_FOLDER_PATH + "/train/images/"
src_label = RAW_YOLO_DATASET_FOLDER_PATH + "/labels/"
dst_label = PREPARED_DATASET_FOLDER_PATH + "/train/labels/"
for i in range(cut_index):
    img_name = all_images[i]
    lable_name = all_lables[i]
    shutil.copyfile(src_img + img_name, dst_img + img_name)
    shutil.copyfile(src_label + lable_name, dst_label + lable_name)
if(cut_index != len(all_images)):
    dst_img = PREPARED_DATASET_FOLDER_PATH + "/val/images/"
    dst_label = PREPARED_DATASET_FOLDER_PATH + "/val/labels/"
    for i in range(cut_index, len(all_images)):
        img_name = all_images[i]
        lable_name = all_lables[i]
        shutil.copyfile(src_img + img_name, dst_img + img_name)
        shutil.copyfile(src_label + lable_name, dst_label + lable_name)

file = open(file=(PREPARED_DATASET_FOLDER_PATH + "/custom_data.yaml"), mode='w')
classes_file = open(file=(RAW_YOLO_DATASET_FOLDER_PATH + "/classes.txt"), mode="r")

file.write("train: " + "../" +  PREPARED_DATASET_FOLDER_PATH + "/train" + "\n")
file.write("val: " + "../"  + PREPARED_DATASET_FOLDER_PATH + "/val" + "\n")

classes_names = [line.strip() for line in classes_file.readlines()]
file.write("nc: " + str(len(classes_names)) + "\n")
t = "[ "
for name in classes_names:
    t += "\"" + name + "\", "
t = t[:-2]
t += " ]"
file.write("names: " + t)
file.close()


import os
import shutil
import math

RAW_DATASET_FOLDER_NAME = "dataset"
DATASET_ROOT_FOLDER_NAME = "pig_dataset"
#value from 0 to 1
train_val_percent = 0.8

if not(os.path.exists(DATASET_ROOT_FOLDER_NAME + "/")):
    os.makedirs(DATASET_ROOT_FOLDER_NAME + "/train/images/")
    os.makedirs(DATASET_ROOT_FOLDER_NAME + "/train/labels/")

    os.makedirs(DATASET_ROOT_FOLDER_NAME + "/val/images/")
    os.makedirs(DATASET_ROOT_FOLDER_NAME + "/val/labels/")

all_images = os.listdir(RAW_DATASET_FOLDER_NAME + "/images")
all_lables = os.listdir(RAW_DATASET_FOLDER_NAME + "/labels")

cut_index = math.floor(len(all_images) * train_val_percent)

src_img = RAW_DATASET_FOLDER_NAME + "/images/"
dst_img = DATASET_ROOT_FOLDER_NAME + "/train/images/"
src_label = RAW_DATASET_FOLDER_NAME + "/labels/"
dst_label = DATASET_ROOT_FOLDER_NAME + "/train/labels/"
for i in range(cut_index):
    img_name = all_images[i]
    lable_name = all_lables[i]
    shutil.copyfile(src_img + img_name, dst_img + img_name)
    shutil.copyfile(src_label + lable_name, dst_label + lable_name)
if(cut_index != len(all_images)):
    dst_img = DATASET_ROOT_FOLDER_NAME + "/val/images/"
    dst_label = DATASET_ROOT_FOLDER_NAME + "/val/labels/"
    for i in range(cut_index, len(all_images)):
        img_name = all_images[i]
        lable_name = all_lables[i]
        shutil.copyfile(src_img + img_name, dst_img + img_name)
        shutil.copyfile(src_label + lable_name, dst_label + lable_name)

file = open(file=(DATASET_ROOT_FOLDER_NAME + "/custom_data.yaml"), mode='w')
classes_file = open(file=(RAW_DATASET_FOLDER_NAME + "/classes.txt"), mode="r")

file.write("train: " + "../" +  DATASET_ROOT_FOLDER_NAME + "/train" + "\n")
file.write("val: " + "../" +  + DATASET_ROOT_FOLDER_NAME + "/val" + "\n")

classes_names = [line.strip() for line in classes_file.readlines()]
file.write("nc: " + str(len(classes_names)) + "\n")
t = "[ "
for name in classes_names:
    t += "\"" + name + "\", "
t = t[:-2]
t += " ]"
file.write("names: " + t)
file.close()

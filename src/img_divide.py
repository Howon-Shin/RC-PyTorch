import cv2
import os
import sys
import random

dir_path = sys.argv[1]

if len(sys.argv) != 2:
    print("no directory")
    sys.exit()

os.chdir(dir_path)
imgs = os.listdir(dir_path)

dir_up = dir_path.rfind('/')
crop_dir = dir_path + "_crop"
print(crop_dir)
if not os.path.exists(crop_dir):
    os.makedirs(crop_dir)
    print(crop_dir + " directory is created")

j = 0
for img in imgs:
    if img[-4:] != '.png':
        continue

    img_data = cv2.imread(img)

    h, w, c = img_data.shape
    h1 = h//3
    w1 = w//3
    h2 = h1*2
    w2 = w1*2

    crop_img = []
    crop_img.append(img_data[0:h1, 0:w1])
    crop_img.append(img_data[0:h1, w1:w2])
    crop_img.append(img_data[0:h1, w2:w])
    crop_img.append(img_data[h1:h2, 0:w1])
    crop_img.append(img_data[h1:h2, w1:w2])
    crop_img.append(img_data[h1:h2, w2:w])
    crop_img.append(img_data[h2:h, 0:w1])
    crop_img.append(img_data[h2:h, w1:w2])
    crop_img.append(img_data[h2:h, w2:w])

    ext_idx = img.rfind('.')
    ext = img[ext_idx:]

    for i in range(9):
        crop_img_name = img[0:ext_idx] + "_crop" + str(i) + ext
        cv2.imwrite(crop_dir + '/' + crop_img_name, crop_img[i])
        #print(crop_dir + '/' + crop_img_name + " is saved")
    j = j + 1
    if (j%100 == 0):
        print(str(j) + "  ---------------------------------------------------")
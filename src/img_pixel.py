import cv2
import os
import sys
import random
import shutil

dir_path = sys.argv[1]

if len(sys.argv) != 2:
    print("no directory")
    sys.exit()

os.chdir(dir_path)
imgs = os.listdir(dir_path)

for i in range(len(imgs)):
    if i >= len(imgs):
        break
    if imgs[i][-4:] != '.png':
        imgs.remove(imgs[i])

pixels = 0
for img in imgs:
    img_data = cv2.imread(img)
    h, w, c = img_data.shape

    pixels = pixels + h*w

print(dir_path + " : " + str(pixels))
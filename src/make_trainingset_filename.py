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

for i in range(len(imgs)):
    if i >= len(imgs):
        break
    if imgs[i][-4:] != '.png':
        imgs.remove(imgs[i])

imgs = random.sample(imgs, len(imgs)//10)
for img in imgs:
    print(img)
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

if len(imgs) > 150:
    imgs = random.sample(imgs, 150)

sam_dir = dir_path + "_sampled"
os.makedirs(sam_dir)

i = 0
for img in imgs:
    shutil.copy(dir_path + '/' + img, sam_dir + '/' + img)
    
    i = i + 1
    if (i%100 == 0):
        print(i)
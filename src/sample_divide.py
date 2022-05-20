import cv2
import os
import sys
import random
import shutil

dir_path = sys.argv[1]  # bpg directory

if len(sys.argv) != 2:
    print("no directory")
    sys.exit()

os.chdir(dir_path)
imgs = os.listdir(dir_path)

img_bpps = {}

for i in range(len(imgs)):
    if i >= len(imgs):
        break
    if imgs[i][-4:] != '.png':
        imgs.remove(imgs[i])

bpp_list = []

for img in imgs:
    bpp_idx = img.rfind("bpp")
    ext_idx = img.rfind('.png')
    img_bpp = img[bpp_idx + 3:bpp_idx + 10]
    img_name = img[:bpp_idx] + img[ext_idx:]
    # print(img_name, img_bpp)

    img_bpps[img_name] = float(img_bpp)

    bpp_list.append(img_bpps[img_name])

bpp_list.sort()
print(bpp_list[len(imgs)//3], bpp_list[len(imgs)//2], bpp_list[len(imgs)//3*2])
# 3.0369 3.88782 4.84027

original_dir = dir_path[:dir_path.rfind("_bpg")]
sm_dir = original_dir + "_sm"
os.makedirs(sm_dir)
tx_dir = original_dir + "_tx"
os.makedirs(tx_dir)

avg_bpp = sum(bpp_list)/len(bpp_list)
print('average: ', avg_bpp) # average:  4.178008277814839

tx = 0
sm = 0
thres = bpp_list[len(imgs)//3]
for filename in img_bpps:
    # if (img_bpps[filename] >= thres):
    if (img_bpps[filename] >= 3.0369):
        shutil.copy(original_dir + '/' + filename, tx_dir + '/' + filename)
        tx = tx + 1
    else:
        shutil.copy(original_dir + '/' + filename, sm_dir + '/' + filename)
        sm = sm + 1

print(sm, tx)
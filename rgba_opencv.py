import cv2

mask_img = cv2.imread("images/otahuku.png", -1)  # この-1はアルファ要素を入れてくれる
print(mask_img)
print(mask_img.shape)

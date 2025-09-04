import numpy as np
import matplotlib.pyplot as plt
import cv2
 
img = cv2.imread('shapes.jpg')
out = img.copy() #ignore status

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #ignore status
out_rgb = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
red_mask= cv2.inRange (out ,np.array([0, 0, 100]),np.array([50,50,255]))
blue_mask= cv2.inRange (out ,np.array([100, 0, 0]),np.array([255,50,50]))
black_mask= cv2.inRange (out ,np.array([0, 0, 0]),np.array([50,50,50]))

out[red_mask>  0] = [255, 0, 0]
out[blue_mask > 0] = [0, 0, 0]
out[black_mask> 0]=[0, 0, 255]
out_rgb = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)

fig, axes = plt.subplots(1, 2)
axes[0].imshow(img_rgb)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(out_rgb)
axes[1].set_title('Processed Image')
axes[1].axis('off')

plt.show()
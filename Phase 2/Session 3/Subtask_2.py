import numpy as np
import matplotlib.pyplot as plt
import cv2
 
img = cv2.imread('shapes.jpg')
out = img.copy() #ignore status

img_rgb = img[..., ::-1] #ignore status
red_mask = (out[..., 2] > 100) & (out[..., 0] < 50) & (out[..., 1] < 50)    # High red, low blue/green
blue_mask = (out[..., 0] > 100) & (out[..., 1] < 50) & (out[..., 2] < 50)    # High blue, low green/red
black_mask = (out[..., 0] < 50) & (out[..., 1] < 50) & (out[..., 2] < 50)    # All channels low

out[red_mask] = [255, 0, 0]     
out[blue_mask] = [0, 0, 0]      
out[black_mask] = [0, 0, 255]   

out_rgb = out[..., ::-1]

fig, axes = plt.subplots(1, 2)
axes[0].imshow(img_rgb)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(out_rgb)
axes[1].set_title('Processed Image')
axes[1].axis('off')

plt.show()
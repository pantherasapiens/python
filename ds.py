import numpy as np
import matplotlib.pyplot as plt
import cv2
img1=np.zeros(shape=(600,800,3),dtype=np.int32)

cv2.rectangle(img1,pt1=(50,100),pt2=(150,250),color=(0,255,0),thickness=2)
plt.imshow(img1)
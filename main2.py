import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread("image.png")
brighter_image=np.ones(image.shape,dtype="uint8")+50
brighter=cv2.add(image,brighter_image)
brighter_colored_image=cv2.cvtColor(brighter,cv2.COLOR_BGR2RGB)
plt.imshow(brighter_colored_image)
plt.title('Brighter image')
plt.show()
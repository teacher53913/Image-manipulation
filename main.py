import cv2
import matplotlib.pyplot as plt
image=cv2.imread("image.png")
#convert to rgb
# image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# plt.imshow(image_rgb)
# plt.title("RGB Image")
# plt.show()
#convert to grayscale
# image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# plt.imshow(image_gray,cmap='gray')
# plt.title("Grayscale image")
# plt.show()
#crop the image
cropped_image=image[100:300,200:400]
#convert to colored image
cropped_colored_image=cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_colored_image)
plt.title("Cropped image")
plt.show()
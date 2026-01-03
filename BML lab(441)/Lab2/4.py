import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

image = cv2.imread("/content/drive/My Drive/ML_Dataset/TUMOR_DATASET1/images/3.png")  
print("Original Shape:", image.shape)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


img_256 = cv2.resize(gray, (256, 256))
img_224 = cv2.resize(gray, (224, 224))


h, w = img_256.shape
cropped = img_256[10:h-10, 10:w-10]


img_float = cropped.astype(np.float32)


img_minmax = img_float / 255.0


mean = np.mean(img_float)
std = np.std(img_float)
img_zscore = (img_float - mean) / std


mask = np.zeros_like(img_256, dtype=np.uint8)
center = (128, 128)
radius = 80
cv2.circle(mask, center, radius, 255, -1)

masked_img = cv2.bitwise_and(img_256, img_256, mask=mask)

plt.imshow(masked_img, cmap='gray')
plt.title("Circular Masked Image")
plt.axis("off")
plt.show()

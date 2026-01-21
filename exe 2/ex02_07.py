import cv2
import matplotlib.pyplot as plt
import numpy as np

def compute_histogram(img):
    hist = np.zeros(256, dtype=int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist[img[i,j]] += 1
    return hist

img_gray = cv2.imread("low_contrast.png", cv2.IMREAD_GRAYSCALE)

hist = compute_histogram(img_gray)

plt.bar(range(256), hist)
plt.title("Histogram of Grayscale Image")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

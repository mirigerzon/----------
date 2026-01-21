import matplotlib.pyplot as plt
import ex02_01 as ex2_01
import ex02_02 as ex2_02    

img = ex2_01.create_gradient_image(256, 256)

bright_np = ex2_02.brighten(img, 50, func="np")
bright_cv2 = ex2_02.brighten(img, 50, func="cv2")

plt.figure(figsize=(10, 3))

plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Brightened with np.add")
plt.imshow(bright_np, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Brightened with cv2.add")
plt.imshow(bright_cv2, cmap='gray')
plt.axis('off')

plt.show()
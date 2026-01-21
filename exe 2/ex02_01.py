import numpy as np
import matplotlib.pyplot as plt

def create_gradient_image(height, width):
    image = np.zeros((height, width), dtype=np.uint8)

    max_sum = (height - 1) + (width - 1)

    for i in range(height):
        for j in range(width):
            image[i, j] = int(255 * (i + j) / max_sum)

    return image


if __name__ == "__main__":
    height = 256
    width = 256

    gradient_image = create_gradient_image(height, width)

    plt.imshow(gradient_image, cmap='gray')
    plt.axis('off')
    plt.show()

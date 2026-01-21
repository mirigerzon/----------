import cv2
import numpy as np

def create_low_contrast_image(fg, bg, shape_color=255, shape_type='circle'):

    img = np.full((256, 256), fg, dtype=np.uint8)

    if shape_type == 'circle':
        center = (128, 128)
        radius = 50
        cv2.circle(img, center, radius, bg, -1)
    elif shape_type == 'rectangle':
        cv2.rectangle(img, (78, 78), (178, 178), bg, -1)
    
    cv2.imshow("Low Contrast Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img

img = create_low_contrast_image(fg=100, bg=105)

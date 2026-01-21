import cv2
import numpy as np

def normalize_image(img):
    """
    מקבלת תמונה בגווני אפור ומחזירה אותה מנורמלת לטווח 0-255.
    """
    img_float = img.astype(np.float32)
    
    min_val = np.min(img_float)
    max_val = np.max(img_float)
    
    normalized = (img_float - min_val) * (255.0 / (max_val - min_val))
    
    return np.clip(normalized, 0, 255).astype(np.uint8)


gray_image = cv2.imread("low_contrast_grayscale_cv2.png", cv2.IMREAD_GRAYSCALE)

if gray_image is None:
    print("Error: couldn't read the grayscale image")
else:
    normalized_img = normalize_image(gray_image)
    
    cv2.imshow("Normalized Image", normalized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imwrite("low_contrast_normalized.png", normalized_img)

    print("Min:", np.min(normalized_img))
    print("Max:", np.max(normalized_img))
    print("Mean:", np.mean(normalized_img))
    print("Range factor:", (np.max(normalized_img) - np.min(normalized_img)) / 255.0)

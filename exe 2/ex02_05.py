import cv2
import numpy as np

# --- 5a. קריאה לתמונה בגווני אפור ---
file_path = "low_contrast.png"
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("Couldn't read the image.")

# --- 5b. הדפסת ערכים מינימום, מקסימום וממוצע ---
min_val, max_val, _, _ = cv2.minMaxLoc(img)
mean_val = np.mean(img)
range_factor = (max_val - min_val) / 255.0

print(f"Min: {min_val}, Max: {max_val}, Mean: {mean_val:.2f}, Range factor: {range_factor:.4f}")

# --- 5c. פונקציה לנרמל תמונה ללא שימוש בפונקציה מוכנה ---
def normalize_image(img):
    img_float = img.astype(np.float32)
    min_val = np.min(img_float)
    max_val = np.max(img_float)
    normalized = (img_float - min_val) * 255.0 / (max_val - min_val)
    return np.clip(normalized, 0, 255).astype(np.uint8)

normalized_img = normalize_image(img)

# --- הצגת התמונה המנורמלת (אופציונלי) ---
cv2.imshow("Normalized Image", normalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

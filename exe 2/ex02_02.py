import numpy as np

def brighten(img, b, func):
    if func == "np":
        # numpy.add – עלול לגלוש (overflow)
        return np.add(img, b)
    
    elif func == "cv2":
        import cv2
        # cv2.add – חוסם בין 0 ל־255
        return cv2.add(img, b)
    
    else:
        raise ValueError("func must be 'np' or 'cv2'")

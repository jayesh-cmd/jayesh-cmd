import cv2, numpy as np
from PIL import Image
from rembg import remove

def prep():
    out = remove(Image.open("source-photo.jpg"))
    out.save("no_bg.png")
    img = cv2.imread("no_bg.png", cv2.IMREAD_UNCHANGED)
    alpha, gray = img[:, :, 3], cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    enhanced = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8)).apply(gray)
    final = np.where(alpha > 100, enhanced, np.ones_like(gray) * 255)
    cv2.imwrite("source-prepped.png", final)

if __name__ == "__main__":
    prep()

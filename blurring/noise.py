from pathlib import Path
import cv2

#original image size was 3500 x 2430
noisy_img = Path("tunnel_withNoise.jpg")
k_size = 3
img = cv2.imread(noisy_img)
resized = cv2.resize(img, (700, 486))
cv2.imwrite(Path("tunnel_withNoise.jpg"), resized)
remove_noise = cv2.medianBlur(resized, k_size)

cv2.imshow("noise", resized)
cv2.imshow("Median Blur", remove_noise)
cv2.waitKey(0)

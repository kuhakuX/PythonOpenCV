#รูปแบบภาพ
import cv2
img = cv2.imread("Pic & Videos/105194786_p0.png",1)  # 0 = GRAY SCALE , 1 = RGB or Color , -1 Alpha channel
img1080 = cv2.resize(img,(1920,1080))

#แสดงภาพ
cv2.imshow("P i c T u r e",img1080)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()

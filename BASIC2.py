#แสดงผลภาพ
import cv2 # cv2 มาจาก package opencv-python ลงด้วย,install with command # pip install opencv-python
img = cv2.imread("Pic & Videos/105194786_p0.png") # img คือตัวแปรตั้งอะไรก็ได้ cv2.imread คำสั่งอ่านรูป จาก ("Pic & Videos/105194786_p0.png")

#แสดงภาพ
cv2.imshow("P i c T u r e",img) # ดึงรูปมาจาก "ตัวแปร" img หรือก็คือ "Pic & Videos/105194786_p0.png"
cv2.waitKey(delay=0) # 5000 = 5 sec.
cv2.destroyAllWindows() # ปิดหน้าต่าง , ปิดรูป

# Open Video with OpenCV                Home _ Twitter_3.mp4
import cv2

cap = cv2.VideoCapture("Pic & Videos/Home _ Twitter_3.mp4")

while (cap.isOpened()):
    check , frame = cap.read() # รับภาพจากกล้อง frame ต่อ frame

    if check == True :
        cv2.imshow("Miku Miku Dance",frame)
        if cv2.waitKey(100) & 0xFF == ord("e"): # cv2.waitKey(100) ปรับความเร็ว Videos ได้
         break
    else :
        break

cap.release()
cv2.destroyAllWindows()

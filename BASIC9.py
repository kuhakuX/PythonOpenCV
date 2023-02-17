# RECORD VIDEO from camera #
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

result = cv2.VideoWriter("output.avi",fourcc,60.0,(1920,1080))

while (cap.isOpened()):
    check , frame = cap.read() # รับภาพจากกล้อง frame ต่อ frame

    if check == True :
        cv2.imshow("Miku Miku Dance",frame) # GRAYSCALEMODE , frame #
        result.write(frame)
        if cv2.waitKey(100) & 0xFF == ord("e"): # cv2.waitKey(100) ปรับความเร็ว Videos ได้
         break

result.release()
cap.release()
cv2.destroyAllWindows()

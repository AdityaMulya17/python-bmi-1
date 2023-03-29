#made a mistake @BloodyBeaver line 9
import cv2

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  
  cv2.imshow('webcam feed' , frame)
  if cv2.waitKey(1) and 0xFF == ord(' '):
    break
    
cap.release()
cv2.destroyAllWindows()

#by using the spacebar you will be able to finish the process of video capturing
#in opencv and the window will closeeeeee
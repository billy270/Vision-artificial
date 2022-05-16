from types import GeneratorType
import cv2 

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)


stop_data = cv2.CascadeClassifier('stop_data.xml') 


while  True:

    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    toy = stop_data.detectMultiScale(gray,
    scaleFactor = 2,
    minNeighbors = 4)

    for(x,y,w,h) in toy :
        cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),2)
        cv2.putText(frame,'stop',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == 27:
        break

cap.realease()
cv2.destroyAllWindows()

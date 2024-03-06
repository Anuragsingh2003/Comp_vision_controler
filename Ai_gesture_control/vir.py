import cv2
import mediapipe as mp
import pyautogui
import time


pTime=0
detector=htm.handDetector(maxHands=1)
wCam,hCam=640,480
cap=cv2.VideoCapture(0) #capturing first video framme or captured data
cap.set(3,wCam)#prop id is 3
cap.set(4,hCam)#prop id is 4

wscrn,hscrn=autopy.screen.size()

while True:
    sucess,img=cap.read()
    img=detector.findHands(img)  
    lmList, bbox=detector.findPosition(img)
    
    if len(lmList)!=0:
        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:]
        
        #3 checking fingrs up
        fingers=detector.fingersUp()
        print(fingers)
        
       #chek only index fing moving 
        if fingers[1]==1 and fingers[2]==0:
            
            
            x3=np.interp(x1, (8, wCam),(8,wscrn))
            y3=np.interp(x1, (8, hCam),(8,hscrn))
            
            autopy.mouse.move(wscrn-x3,y3)
            cv2.circle(img,(x1))
            
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN, 3,
               (255,0,0), 3)
    cv2.imshow('Virtual ms', img) #resposible to captured img or video
    cv2.waitKey(1) #if u did use 1 it will not show live rec instead will show img one by one
    
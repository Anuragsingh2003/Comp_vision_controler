import cv2
import mediapipe as mp
import pyautogui

cap=cv2.VideoCapture(0) #capturing first video framme or captured data
hand_detector=mp.solutions.hands.Hands()
drawing_points=mp.solutions.drawing_utils

full_screen_width, full_screen_height=pyautogui.size()
index_y=0
while True:
    _, frame =cap.read() #reading video data or capture data
    frame_height,frame_width, _ =frame.shape #from shape we get widhth of current python gui screen only not full window or screen width 
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)# ''  ' ' height of current py gui app
    
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_points.draw_landmarks(frame,hand)#for drawnig points on hands
            landmarks=hand.landmark #geting or storing up all landmarks with id or points of our hands
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width) #for setting up cursor or mouse pointer to only gui screen
                y=int(landmark.y*frame_height)# ""  ""   ""
                
                #we know that all pointers or id of our hand start from 0 to n and , we can calculate acordingly and for indx fingr to pointer id=8
                if id==8: #setting up yellow circle in our index fir by targeting it by id
                    cv2.circle(img=frame,center=(x,y), radius=20,color=(0,255,255))
                    index_x=full_screen_width/frame_width*x
                    index_y=full_screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)
                
                if id==12: #setting up yellow circle in our index fir by targeting it by id
                    cv2.circle(img=frame,center=(x,y), radius=20,color=(0,255,255))
                    thumb_x=full_screen_width/frame_width*x
                    thumb_y=full_screen_height/frame_height*y    
                    print(abs(index_y-thumb_y))

                    if abs(index_y-thumb_y) <40: #if lenght or height of thub and inx finger will meet or very less do click func
                        print('click')
                        pyautogui.click()
                        pyautogui.sleep(1)
                
    cv2.imshow('Virtual ms', frame) #resposible to captured img or video
    cv2.waitKey(1) #if u did use 1 it will not show live rec instead will show img one by one
import numpy as np 
import cv2 
  
cap = cv2.VideoCapture(0) 
panel= np.zeros([100,700], np.uint8)
cv2.namedWindow('panel')

def nothing(x):
   pass

 
cv2.createTrackbar('L - h', 'panel', 0,179, nothing)
cv2.createTrackbar('U - h', 'panel', 179,179, nothing)

cv2.createTrackbar('L - s', 'panel', 0,255, nothing)
cv2.createTrackbar('U - s', 'panel', 255,255, nothing)

cv2.createTrackbar('L - v', 'panel', 0,179, nothing)
cv2.createTrackbar('U - v', 'panel', 255,255, nothing)

cv2.createTrackbar('S ROWS', 'panel', 0, 480, nothing)
cv2.createTrackbar('E ROWS', 'panel', 480, 480, nothing)
cv2.createTrackbar('S COL', 'panel', 0, 640, nothing)
cv2.createTrackbar('E COL', 'panel', 640, 640, nothing)

#fgbg = cv2.createBackgroundSubtractorMOG2() 
  
while(1): 
    _, frame = cap.read()

    s_r = cv2.getTrackbarPos('S ROWS', 'panel')
    e_r = cv2.getTrackbarPos('E ROWS', 'panel')
    s_c = cv2.getTrackbarPos('S COL', 'panel')
    e_c = cv2.getTrackbarPos('E COL', 'panel')
    roi = frame[s_r:e_r, s_c:e_c]
    
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h= cv2.getTrackbarPos('L - h', 'panel')
    u_h= cv2.getTrackbarPos('U - h', 'panel')
    l_s= cv2.getTrackbarPos('L - s', 'panel')
    u_s= cv2.getTrackbarPos('U - s', 'panel')
    l_v= cv2.getTrackbarPos('L - v', 'panel')
    u_v= cv2.getTrackbarPos('U - v', 'panel')
  

    lower_green= np.array([l_h, l_s, l_v])
    upper_green= np.array([u_h, u_s, u_v])
    

    mask= cv2.inRange(hsv, lower_green, upper_green) 
    mask_inv = cv2.bitwise_not(mask)
    #fgmask = fgbg.apply(frame)

    
    bg= cv2.bitwise_and(frame, frame, mask=mask) #bitwise is an op which is taking an argument and filtering it with mask
    fg= cv2.bitwise_and(frame, frame, mask=mask_inv)
   
    cv2.imshow('bg', bg) 
    cv2.imshow('fg', fg) 
    cv2.imshow('panel', panel)
    
    key = cv2.waitKey(200)
    if key in [ord('a'), 1048673]:
        nothing
    elif key in [27, 1048603]: # ESC key to abort, close window
        cv2.destroyAllWindows()
        break
     
  
cap.release() 
cv2.destroyAllWindows() 

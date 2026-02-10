import cv2
import numpy as np
# img = cv2.imread('SMITFig.png')

# cv2.imshow("testing",img)

# cv2.waitKey(0)

# cv2.destroyAllWindowS()


## ----- color based object detection ------

# capture = cv2.VideoCapture(0)

# if capture.isOpened():
#     while(cv2.waitKey(3) != ord('q')):
#         ret, frame = capture.read()
#         if ret:
#             # edges = cv2.Canny(frame,50,300)
#             # lines =  cv2.HoughLinesP(edges,1,np.pi/180,200,100,10)
            
#             # for x1, y1, x2, y2 in lines[:,0,:]:
#             #     cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)
#             # cv2.imshow('lines',frame)

#             hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#             lowBound =  np.array([110,50,50])
#             upBound  = np.array([130,255,255])

#             mask  = cv2.inRange(hsv_img,lowBound,upBound)

#             kernel = np.ones((5,5), np.uint8)
#             mask = cv2.dilate(mask,kernel,iterations=1)

#             h1,w1 = mask.shape
#             h2,w2,d2 = frame.shape
#             img_to_show = np.zeros((max(h1,h2),w1+w2,3), dtype = 'uint8')
#             img_to_show[:h1,:w1,0] = mask
#             img_to_show[:h1,:w1,1] = mask
#             img_to_show[:h1,:w1,2] = mask
#             img_to_show[:h2,w1:w1+w2,:] = np.dstack([frame])

#             cv2.imshow("my image",img_to_show)

#     cv2.destroyAllWindowS()
# else:
#     print("something happend on webcam!!")


## ----- find color shape object ------

# cap = cv2.VideoCapture(0)

# if cap.isOpened():
#     while cv2.waitKey(3) != ord('q'):
#         ret, frame= cap.read()
#         if ret != True:
#             print('something happend!!')
#             break
#         hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         # set up lower and upper bound for color range of blue
#         lowBound = np.array([100, 50, 50])
#         upBound = np.array([130, 255, 255])
#         #filtering by color
#         mask = cv2.inRange(hsv_image,lowBound,upBound)
#         #image dilation
#         kernel = np.ones((3,3),np.uint8)
#         mask = cv2.dilate(mask, kernel, iterations = 1)
#         cnts, flag = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:2] #2
#         for c in cnts:
#             peri = cv2.arcLength(c, True)
#             approx = cv2.approxPolyDP(c, 0.01*peri, True)
#             if (len(approx)==4): # if it is 4-sides polygon
#                 cv2.drawContours(frame, [approx],0,(0,255,0),-1)
#             if (len(approx)>10):
#                 cv2.drawContours(frame, [approx],0,(0,0,255),-1)

#         # h1,w1 = mask.shape
#         # h2,w2,d2 = frame.shape
#         # imgCom = np.zeros((max([h1,h2]),w1+w2,3), dtype = np.uint8)
#         # imgCom[:h1,:w1,0] = mask
#         # imgCom[:h1,:w1,1] = mask
#         # imgCom[:h1,:w1,2] = mask
#         # imgCom[:h2,w1:w1+w2,:] = np.dstack([frame])
#         #image resize
#         # imgCom = cv2.resize(imgCom,(w1,h1),interpolation = cv2.INTER_LINEAR)
#         cv2.imshow( "webCom",frame) 
        
        
# cap.release()
# cv2.waitKey(0)
# cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)

if cap.isOpened():
    face= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    while cv2.waitKey(3) != ord('q'):
        ret, frame= cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray,1.3,5)
        eyes = eye.detectMultiScale(gray,1.3,2)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(20,206,80), 2)
        
        for (x,y,w,h) in eyes:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(20,80,220), 2)

        cv2.imshow("face detect", frame)
    cv2.destroyAllWindows()





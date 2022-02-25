import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt 
from tkinter import *

ycoord = [0]
xcoord = [0]
counter = 0
count = 0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')
video_capture = cv2.VideoCapture(0)

while True:
    counter = counter + 1

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

    try:
        w
    except NameError:
        print("FACE IS NOT DETECTED WITHIN THE FRAME.")
    else:
        if len(faces) <= 0:
            ycoord.append(int(0))  
            xcoord.append(int(counter))
        elif len(faces) >= 0:
                if w>= 250:
                    if len(eyes)>0:
                       ycoord.append(int(100))
                    else:
                        ycoord.append(int(95))
                    xcoord.append(int(counter))
                    count = count + 1
                elif w<=40:
                    if len(eyes)>0:
                        ycoord.append(int(10))
                    else:
                        ycoord.append(int(5)) 
                    xcoord.append(int(counter))
                    count = count + 1
                elif w>40 and w<= 50:
                    if len(eyes)>0:
                        ycoord.append(int(15))
                    else:
                        ycoord.append(int(10))
                    xcoord.append(int(counter))
                    count = count + 1
                else:
                    val = (w/250) * 100
                    if len(eyes)>0 and val<=90:
                        ycoord.append(int(val)+10)
                    else:
                        ycoord.append(int(val))                   
                    xcoord.append(int(counter))
                    count = count + 1
        
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

Efficiency = int((count/len(xcoord))*100)
Result = str(Efficiency) + "%"

plt.scatter(xcoord,ycoord,label="marker",color="black", marker= ".", s=30)

plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.title("Face Detection Efficiency Graph")
plt.legend()

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

plt.show()

root = Tk()
root.title("Face Detection Efficiency")
root.iconbitmap('c:/Users\swara\Documents\Program Code\Python\Gallery.ico') 

def ClickedButton():
    myLabel = Label(root, text = Result)
    myLabel.pack()

frame = LabelFrame(root, text= "To check your attentiveness: ", padx=10, pady=10)
frame.pack(padx=15, pady=15)

simple_button=Button(frame, text="Click Here", command=ClickedButton, fg="black", bg="white")
simple_button.pack()
root.mainloop()
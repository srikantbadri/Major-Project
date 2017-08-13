#Working with Webcam Feed
import cv2
import numpy as np

#Capturing video from 1st webcam
#0-1stWebcam
#1-2ndWebcam
cap=cv2.VideoCapture(0)

#For saving the video to output.avi
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while (True):
	
	ret, frame=cap.read()
	
	#converting image to grayscale
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	out.write(frame)
	
	#showing image continuously
	cv2.imshow('frame',frame)	#natural
	cv2.imshow('gray',gray)		#grayscale
	
	if cv2.waitKey(1) & 0xFF==ord('q'):  #q to Quit
		break

cap.release()
out.release()
cv2.destroyAllWindows()

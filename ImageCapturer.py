import cv2, sys
sys.path.append('/home/kelly/Code/cv')
import numpy as np
from StillStarter import StillStarter
from FaceRecognizer import FaceRecognizer
from Queue import Queue

img_queue = Queue(maxsize = 5)
rtn_queue = Queue(maxsize = 5)

start_still_cap = StillStarter(1,cv2,img_queue)

c = cv2.VideoCapture(0)
_, f = c.read()


avg = np.float32(f)
avg2= np.float32(f)
dif  = np.float32(f)

recognizer = FaceRecognizer(img_queue,rtn_queue)
recognizer.start_thread()


while 1:
	_, f = c.read()

	cv2.accumulateWeighted(f,avg,0.3)
	cv2.accumulateWeighted(f,avg2,0.7)

	dif = f-avg

	res1 = cv2.convertScaleAbs(avg)
	res2 = cv2.convertScaleAbs(avg2)
	res3 = cv2.convertScaleAbs(dif)

	cv2.imshow('img',f)
	#cv2.imshow('Dif',res3)
	k = cv2.waitKey(20)

	move_value = np.sum(dif)

	if move_value > 1000000:
		#print "Movement!", move_value
		start_still_cap(0.5,c)

	if k == 27:
		img_queue.put(None)
		break

cv2.destroyAllWindows()
c.release
import cv, cv2, sys
sys.path.append('/home/kelly/Code/cv')
import numpy as np
from StillStarter import StillStarter
from FaceRecognizer import FaceRecognizer
from Queue import Queue, Empty
from threading import Thread

def capture_images(inqueue,return_queue):
	'''Captures images of faces from webcam, putting them in return_queue. To end the process,
	inqueue.put(None). Lives in its own thread.'''

	def run():
		'''Does all the dirty work, so we can make a thread.'''

		img_queue = Queue(maxsize = 5)

		start_still_cap = StillStarter(1,cv2,img_queue)

		c = cv2.VideoCapture(0)
		_, f = c.read()

		avg = np.float32(f)
		dif  = np.float32(f)

		recognizer = FaceRecognizer(img_queue,return_queue)
		recognizer.start_thread()

		done = 1
		while done != None:

			try: done = inqueue.get(block=False)
			except Empty: pass
			_, f = c.read()

			cv2.accumulateWeighted(f,avg,0.3)

			dif = f-avg

			res3 = cv2.convertScaleAbs(dif)

			## Uncomment to show webcam video
			## cv2.imshow('img',f)

			## Uncomment to show the difference between f and avg
			## cv.ShowImage('Dif',cv.fromarray(dif))
			k = cv2.waitKey(20)

			move_value = np.sum(dif)

			if move_value > 1000000:
				#print "Movement!", move_value
				start_still_cap(0.5,c)

			if k == 27 or done ==  None:
				img_queue.put(None)
				break

		cv2.destroyAllWindows()
		c.release()

	t = Thread(target = run)
	t.start()
	return

if __name__ == '__main__':			## Just wait for 5 images to be captured						
	out = Queue(maxsize=5)			## Then kill the thread
	kill_queue  = Queue(maxsize=1)
	capture_images(kill_queue,out)
	for x in range(5):
		print x
		out.get()
	kill_queue.put(None)


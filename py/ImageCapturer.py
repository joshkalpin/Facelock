import cv, cv2, sys
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

		img_queue = Queue(maxsize = 5)						## Spawns threads which capture
		start_still_cap = StillStarter(1,cv2,img_queue)		## images, putting in img_queue
		c = cv2.VideoCapture(0)
		_, f = c.read()										## store raw cam data in f

		avg = np.float32(f)									## declare memory for math ops
		dif  = np.float32(f)

		recognizer = FaceRecognizer(img_queue,return_queue) ## Initialize facial recognition
		recognizer.start_thread()							## thread

		done = 1											## Loop watches for movement,
		while done != None:									## searching for faces if there
															## is any
			try: done = inqueue.get(block=False)
			except Empty: pass
			_, f = c.read()

			cv2.accumulateWeighted(f,avg,0.3)				## Put results of average over
															## time into avg

			dif = f-avg										## Difference between f and avg
															## to find movement
			res3 = cv2.convertScaleAbs(dif)
			move_value = np.sum(dif)

			## Uncomment to show webcam video
			## cv2.imshow('img',f)

			## Uncomment to show the difference between f and avg
			## cv.ShowImage('Dif',cv.fromarray(dif))


			if move_value > 1000000:
				#print "Movement!", move_value
				start_still_cap(1,c)


			k = cv2.waitKey(20)								## Poll for close event
			if k == 27 or done ==  None:
				img_queue.put(None)
				break

		cv2.destroyAllWindows()								## Close windows when loop
		c.release()											## terminates

	t = Thread(target = run)								## Live in your own thread
	t.start()
	return

if __name__ == '__main__':			## Just wait for 5 images to be captured						
	out = Queue(maxsize=10)			## Then kill the thread
	kill_queue  = Queue(maxsize=1)
	capture_images(kill_queue,out)
	for x in range(5):
		print x
		im = out.get()
		cv.ShowImage('face',im)		## Show face if we find one
		while 1:
			k = cv2.waitKey()
			print k
			if k == 27:
				cv2.destroyAllWindows()
				break
	kill_queue.put(None)


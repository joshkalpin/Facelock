from threading import Timer


class StillStarter:

	def __init__(self,max, cv2, outqueue):
		''' max is the max number of threads to allow. cv2 is a cv2 namespace, outqueue
		is used to pass data between threads'''
		self.queue = outqueue
		self.max = max
		self.cur = 0
		self.cv2 = cv2

	def __call__(self,time,c):			## Only allow one call at a time, to stop
		if self.cur < self.max:			## pointless computation
			self.cur += 1

										## Take picture time after call
			wait_timer = Timer(time, self.cap_img, args = (c,))
			wait_timer.start()			

	def cap_img(self,c):
		_, img = c.read()				## Take picture
		self.queue.put(img)				## Send to FaceRecognizer

		self.cur -= 1					## Allow next call
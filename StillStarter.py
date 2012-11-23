from threading import Timer,active_count

class StillStarter:

	def __init__(self,max, cv2, outqueue):
		self.queue = outqueue
		self.max = max
		self.cur = 0
		self.cv2 = cv2

	def __call__(self,time,c):
		if self.cur < self.max:
			self.cur += 1
			wait_timer = Timer(time, self.cap_img, args = (c,))
			wait_timer.start()

	def cap_img(self,c):
		_, img = c.read()
		#self.cv2.imshow('Still',img)
		self.queue.put(img)
		self.cur -= 1
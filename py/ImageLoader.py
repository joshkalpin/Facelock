import sqlite3 as sql

class Image:

	def __init__(self, iid, created, image, sid):
		self.iid = iid
		self.created = created
		self.image = image
		self.sid = sid

class ImageController:

	def __init__(self):
		self.images = []
		self.connection = sql.connect('../db/facelock.db')
		self.load_images()

	def load_images(self):
		cursor = self.connection.cursor()
		for iid, created, image, sid in cursor.execute("SELECT * FROM Image"):
			self.images.append(Image(iid, created, image, sid))

		return self.images

	def is_empty(self):
		return self.images == []

	def addImage(self, image):
		cursor = self.connection.cursor()
		cursor.execute("INSERT INTO Image VALUES (%s, \'%s\', \'%s\', \'%s\')" % (image.iid, image.created, image.image, image.sid))
		self.connection.commit()

if __name__ == '__main__':
	i = ImageController()
	i.is_empty()
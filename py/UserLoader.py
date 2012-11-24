import sqlite3 as sql

class User:

	def __init__(self, uid, name, created, password):
		self.uid = uid
		self.name = name
		self.created = created
		self.password = password

class UserController:

	def __init__(self):
		self.users = []
		self.connection = sql.connect('../db/facelock.db')
		self.load_users()

	def load_users(self):
		cursor = self.connection.cursor()
		for uid, name, created, password in cursor.execute("SELECT * FROM User"):
			self.users.append(User(uid, name, created, password))

		return self.users

	def is_empty(self):
		return self.users == []

	def addUser(self, new_user):
		cursor = self.connection.cursor()
		cursor.execute("INSERT INTO User VALUES (%s, \'%s\', \'%s\', \'%s\')" % (new_user.uid, new_user.name, new_user.created, new_user.password))
		self.connection.commit()

	def removeUser(self, user):
		cursor = self.connection.cursor()
		cursor.execute("DELETE FROM User WHERE created = %s" % user.created)
		self.connection.commit()
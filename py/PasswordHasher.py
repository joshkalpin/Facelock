import hashlib
import uuid

class PasswordHasher:

	def __init__(self):
		self.salt = uuid.uuid4().hex

	def encode(self, password):
		return hashlib.sha512(password + self.salt).hexdigest()

	def is_match(self, password, pw_hash):
		return encode(password) == pw_hash
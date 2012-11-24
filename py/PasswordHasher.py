import hashlib
import uuid

class PasswordHasher:

	def encode(self, password):
		return hashlib.sha512(password).hexdigest()

	def is_match(self, password, pw_hash):
		return encode(password) == pw_hash
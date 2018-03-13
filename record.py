class Record:
	"""
	This class represents a record.

	:param key : The key of the record.
	:type n : int
	:param data : The data of the record (optional).
	:type data : str
	"""

	def __init__(self, key, data=''):
		self.key = key
		self.data = data

	def key(self):
		return self.key

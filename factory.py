import random
from record import Record


class Factory:
	"""
	This class generates a list of records

	:param n : The length of the list
	:type n : int
	:param order : {'ascending', 'descending', 'random'}. Default is ascending
	:type order : str
	:param mode : {'empty', 'filled'} If 'filled', fills the records with some data. Default is 'empty'.
	:type mode : str
	:param size : The number of lines of the record's data
	:type size : int
	"""

	size = 50

	def __init__(self, n, order='ascending', mode='empty'):
		self.n = n
		self.order = order
		self.mode = mode

	def make_record(self, key):
		"""
		Generates a record to be inserted in the list.
		If the class param <mode> is 'filled', the record will be filled with some data

		:param key : The key of the record
		:return : A record with the key that can have an amount of data
		:rtype : Record
		"""
		data = None
		if self.mode == 'filled':
			data = self.fill_record()

		record = Record(key, data)
		return record

	def fill_record(self):
		"""
		Generates the data for a record

		:return : The data of the record
		:rtype : str
		"""
		data = self.size * '..................................................\n'
		return data

	def make_list(self):
		"""
		Uses the class parameters to generate a list of records.
		The list can be in ascending, descending or random order.

		:return : a list of size n
		:rtype : list
		"""
		list = []
		for i in range(self.n):
			register = self.make_record(i + 1)
			list.append(register)
		if self.order == 'random':
			random.shuffle(list)
		elif self.order == 'descending':
			list.reverse()
		return list


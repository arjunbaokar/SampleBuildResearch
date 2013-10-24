class Vector():

	def __init__(self, col_values = None):
		if col_values != None:
			self.colValues = col_values
		else:
			self.colValues = []

	def __len__(self):
		return len(self.colValues)

	def get(self,n):
		return colValues[n]

	def add(self, n):
		colValues += [n]

	def insert(self, index, value):
		self.colValues[index] = value

	def toList(self):
		return self.colValues
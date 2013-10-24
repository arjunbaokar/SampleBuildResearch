class Vector():

	def __init__(self, col_values = None):
		if col_values != None:
			self.colValues = col_values
		else:
			self.colValues = []

	def __len__(self):
		return len(self.colValues)

	def get(n):
		return colValues[n]

	def add(n):
		colValues += [n]

	def insert(index, value):
		self.colValues[index] = value

	def toList():
		return self.colValues



'''
Optimized for getting columns, not rows.
Input: list of vectors, rank of the Matrix
'''
class Matrix():

	def __init__(self, vectors, inputRank=None):
		self.vectorList = vectors
		self.rank = inputRank

	def numCols():
		return len(self.vectorList[0])

	def numRows():
		return len(self.vectorList)

	def rank():
		return self.rank

	def getRow(n):
		buildVector = Vector()
		for i in range(0,len(self.vectorList)):
			buildVector.add(self.vectorList[i][n])
		return buildVector

	def getCol(j):
		return self.vectorList[j]

	def get(i,j):
		return self.vectorList[i].get[j]

	def set(col,row, value):
		self.vectorList[col].insert(row,value)



'''
Modelled after a Thread in Java; you can instantiate algorithms with data, and call them from a run method. They are also independent of the calculator and can be parallelized.
Need a dataset, which can be specified for the Algorithm. This makes it easy to add more Algorithms.
All algorithms can extend Algorithm.

REQUIRED:
runAlgorithm() which runs the algorithm on the dataset. This can call other methods and be a parallelized method. Must be threadsafe.
'''
class Algorithm(object):

	def runAlgorithm():
		#bulk of the code goes here
		pass
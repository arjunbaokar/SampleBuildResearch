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
		for i in range len(self.vectorList):
			buildVector.add(self.vectorList[i][n])
		return buildVector

	def getCol(j):
		return self.vectorList[j]

	def get(i,j):
		return self.vectorList[i].get[j]

	def set(col,row, value):
		self.vectorList[col].insert(row,value)

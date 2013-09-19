'''
Optimized for getting columns, not rows.
'''
class Matrix():

	def __init__(self, vectors):
		self.vectorList = vectors

	def numCols():
		return len(self.vectorList[0])

	def numRows():
		return len(self.vectorList)

	def rank():
		return None # IMPLEMENT THIS

	def getRow(n):
		buildVector = Vector()
		for i in range len(self.vectorList):
			buildVector.add(self.vectorList[i][n])
		return self.vectorList[i]

	def getCol(j):
		return self.vectorList[j]

	def get(i,j):
		return self.vectorList[i].get[j]

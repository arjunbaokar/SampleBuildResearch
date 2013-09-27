import random
import math

class BourgainEmbeddingAlgorithm(Algorithm):

	def __init__(self, targetMatrix, desiredRank):
		self.matrix = targetMatrix
		self.targetRank = desiredRank

	def runAlgorithm():
		m1 = matrix.numCols()
		m2 = math.log(m1)
		randSet = set()
		for i in range(1,m1+1):
			for j in range(1,m2+1):
				 if (useCurrentNumber(i)):
				 	randSet.add(1239481293047129834701293) #x in V, find a way to figure out what x in V is




	# Decides if current number will be used in algorithm. Returns true with P(X) = 2**-i, where i is supplied by the caller
	def useCurrentNumber(i):
		if 1 == random.randrange(2**i):
			return True
		return False


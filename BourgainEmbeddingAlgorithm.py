import random
import math

class BourgainEmbeddingAlgorithm(Algorithm):

	def __init__(self, startingDim, points, numPointsToProject):
		self.V = points
		self.n = numPointsToProject
		self.m1 = None
		self.m2 = None
		if startingDim <= 4:
			self.m1 = startingDim
			self.m2 = 1
		else:
			self.m1 = startingDim**(0.5)
			self.m2 = m1

	def runAlgorithm(self):
		if self.m1 == None or self.m2 == None:
			print "m1 and m2 are null, algorithm will do nothing"

		A = self.constructRandSet()
		m = []

		for i in range(0,self.m1):
			for j in range(0,self.m2):
				m[i][j] = self.minDist(V,A[i][j])


	def minDist(self, x, y):
		#TODO: IMPLEMENT THIS
		#take Euclidean distance between V and A, find minimum of that
		pass


	def constructRandSet(self):
		toReturn = set()
		for i in range (0,len(V)):
			if useCurrentNumber(i):
				toReturn.add(V[i])
		return toReturn


	# Decides if current number will be used in algorithm. Returns true with P(X) = 2**-i, where i is supplied by the caller
	def useCurrentNumber(i):
		if 1 == random.randrange(2**i):
			return True
		return False


import random
import math
import api
import sys

class BourgainEmbeddingAlgorithm(api.Algorithm):

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
				m[i][j] = self.minDist(self.V,A[i][j])

		return m


	def minDist(self, V, Ai):
		#take Euclidean distance between V and A, find minimum of that
		minSoFar = sys.maxsize
		for x in V:
			euclidDist = 0
			if type(Ai) == list:
				for i in range(0,len(x)):
					euclidDist += (Ai[i]-x[i])**2
			else:
				for i in range(0,len(x)):
					euclidDist += (Ai-x[i])**2
			euclidDist = euclidDist**0.5
			if euclidDist < minSoFar:
				minSoFar = euclidDist
		
		return minSoFar


	def constructRandSet(self):
		toReturn = []
		for i in range (0,len(self.V)):
			if self.useCurrentNumber(i):
				toReturn.append(self.V[i])
		return toReturn


	# Decides if current number will be used in algorithm. Returns true with P(X) = 2**-i, where i is supplied by the caller
	def useCurrentNumber(self,i):
		if 1 == random.randrange(2**i):
			return True
		return False


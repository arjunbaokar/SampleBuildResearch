import mdp
import numpy
import api

class PrincipalComponentAnalysis(Algorithm):

	def __init__(targetMatrix, desiredDim):
		self.targetDimension = desiredDim
		self.matrix = targetMatrix

	def setTargetMatrix(targetMatrix):
		self.matrix = targetMatrix

	def setTargetDimension(desiredDim):
		self.targetDimension = desiredDim

	def runAlgorithm():
		if (self.targetDimension == None):
			print "Error: No target dimension set. Please use setTargetDimension(d) to specify matrix."
		elif (self.matrix == None):
			print "Error: No input matrix. Please use setTargetMatrix(M) to specify a target matrix."
		else:
			twoDimList = [];
			for i in range (0,self.matrix.numRows()):
				twoDimList.append(self.matrix.getRow(i).toList())
			print twoDimList

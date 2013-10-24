import mdp
import numpy
import api

class PrincipalComponentAnalysis(api.Algorithm):

	def __init__(self, inputDim, targetMatrix, desiredDim):
		self.startingDimension = inputDim
		self.matrix = targetMatrix
		self.targetDimension = desiredDim

	def setTargetMatrix(targetMatrix):
		self.matrix = targetMatrix

	def setTargetDimension(desiredDim):
		self.targetDimension = desiredDim

	def trainNode(self, node):
		if node.is_trainable():
			x = numpy.random.random((100, self.startingDimension))  # 25 variables, 100 observations
			node.train(x)
			node.stop_training()
			print "output_dim: " + str(node.output_dim)
			print "var: " + str(node.explained_variance)

	def runAlgorithm(self):
		if (self.targetDimension == None):
			print "Error: No target dimension set. Please use setTargetDimension(d) to specify matrix."
		elif (self.matrix == None):
			print "Error: No input matrix. Please use setTargetMatrix(M) to specify a target matrix."
		else:
			twoDimList = [];
			for i in range (0,self.matrix.numRows()):
				twoDimList.append(self.matrix.getRow(i).toList())
			
			prePcaMatrix = numpy.array(twoDimList, dtype='float64')
			pcaNode = mdp.nodes.PCANode(input_dim=self.startingDimension ,output_dim=self.targetDimension, dtype='float64')
			self.trainNode(pcaNode)
			pcaResult = pcaNode(prePcaMatrix)
			return pcaResult

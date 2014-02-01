from sklearn.decomposition import PCA
import numpy
import api

class ScikitPCA(api.Algorithm):

	def __init__(self, targetMatrix, nComponents):
		self.matrix = targetMatrix
		self.numComponents = nComponents

	def setTargetMatrix(self, targetMatrix, inputDim):
		self.matrix = targetMatrix
		self.startingDimension = inputDim

	def setTargetDimension(self, desiredDim):
		self.targetDimension = desiredDim

	def runAlgorithm(self):
		pca = PCA(n_components=self.numComponents)
		pca.fit(self.matrix)
		#return pca.explained_variance_ratio_
		#return pca.explained_variance_
		return pca.components_
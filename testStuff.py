''' Basic script to test new functionality/algorithms.
Edit as you please; this is not important to the framework itself.'''

from api import *
import numpy
from PrincipalComponentAnalysis import PrincipalComponentAnalysis
#from BourgainEmbeddingAlgorithm import BourgainEmbeddingAlgorithm
from ScikitPCA import ScikitPCA

v0 = Vector([1,0,0,0])
v1 = Vector([0,1,0,0])
v2 = Vector([0,0,1,0])
v3 = Vector([0,0,0,1])

a4x4 = Matrix([v0,v1,v2,v3], 4)
b4x4 = [[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,0,1,1]]
c4x4 = numpy.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

pcaAlgo = ScikitPCA(c4x4, 2)
#bourgAlgo = BourgainEmbeddingAlgorithm(b4x4, 4, 2)
result = pcaAlgo.runAlgorithm()
print str(result)
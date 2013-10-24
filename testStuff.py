from api import *
from PrincipalComponentAnalysis import PrincipalComponentAnalysis

v0 = Vector([1,0,0,0])
v1 = Vector([0,1,0,0])
v2 = Vector([0,0,1,0])
v3 = Vector([0,0,0,1])

#Matrix a4x4 = Matrix([, Vector([0,1,0,0]), Vector([0,0,1,0]), Vector([0,0,0,1])], 4)
a4x4 = Matrix([v0,v1,v2,v3], 4)

pcaAlgo = PrincipalComponentAnalysis(a2x2, 2)
result = pcaAlgo.runAlgorithm()
print str(result)
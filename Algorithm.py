'''
Modelled after a Thread in Java; you can instantiate algorithms with data, and call them from a run method. They are also independent of the calculator and can be parallelized.
Need a dataset, which can be specified for the Algorithm. This makes it easy to add more Algorithms.
All algorithms can extend Algorithm.

REQUIRED:
runAlgorithm() which runs the algorithm on the dataset. This can call other methods and be a parallelized method. Must be threadsafe.
'''
class Algorithm(object):

	def runAlgorithm():
		#bulk of the code goes here
		pass
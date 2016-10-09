from operator import add
from Evolver import Evolver
class Example(Evolver):
	"""docstring for Evolver"""
	#Override 'individual', 'fitness', 'mutate','crossover'
	#Use evolve(), evolveuntilmax(), evolveuntilaverage()
	def __init__(self, count):
        evolver.__init__(self,count)

	def individual(self):
		length = 5
		min = 0
		max = 100
		return [ randint(min,max) for x in xrange(length) ]

	def fitness(self, individual):
		target = 371
		sum = reduce(add, individual, 0)
		return abs(target-sum)

	def mutate(self, individual):
		pos_to_mutate = randint(0, len(individual)-1)
		individual[pos_to_mutate] = randint(min(individual), max(individual))
		return individual

	def crossover(self, male, female):
		half = len(male) / 2
		child = male[:half] + female[half:]
		return child

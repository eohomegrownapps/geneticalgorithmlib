from random import randint, random
from operator import add

class Evolver():
	"""docstring for Evolver"""
	#Override 'individual', 'fitness', 'mutate','crossover'
	#Use evolve(), evolveuntilmax(), evolveuntilaverage()
	def __init__(self, count):
		self.population = []
		self.populate(count)

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

	def grade(self):
		summed = reduce(add, (self.fitness(x) for x in self.population))
		return summed / (len(self.population) * 1.0)

	def populate(self, count):
		self.population = [ self.individual() for x in xrange(count) ]
		return self.population

	def evolve(self, retain=0.2, random_select=0.05, mutate=0.01):
		graded = [ (self.fitness(x), x) for x in self.population]
		graded = [ x[1] for x in sorted(graded)]
		retain_length = int(len(graded)*retain)
		parents = graded[:retain_length]
		# randomly add other individuals to
		# promote genetic diversity
		for individual in graded[retain_length:]:
			if random_select > random():
				parents.append(individual)
		# mutate some individuals
		for individual in parents:
			if mutate > random():
				self.mutate(individual)
		# crossover parents to create children
		parents_length = len(parents)
		desired_length = len(self.population) - parents_length
		children = []
		while len(children) < desired_length:
			male = randint(0, parents_length-1)
			female = randint(0, parents_length-1)
			if male != female:
				child = self.crossover(parents[male],parents[female])
				children.append(child)
		parents.extend(children)
		self.population = parents
		return self.population

	def view(self):
		return self.population

	def evolveuntilmax(self, limit):
		print self.population[0]
		f = self.fitness(self.population[0])
		print f
		while f>limit:
			self.evolve()
			f = self.fitness(self.population[0])
			print self.population[0]
			print f

	def evolveuntilaverage(self, limit):
		print self.population[0]
		f = self.grade()
		print f
		while f>limit:
			self.evolve()
			f = self.grade()
			print self.population[0]
			print f

	def reset(self, count):
		self.populate(count)

import random as rand
import pprint as pp
import numpy as np

from agent import Agent

class DE(object):
    """docstring for DE"""
    def __init__(self,
        npopulation,
        ngenerations,
        func_eval,
        *,
        ub=(5, 5), # search-space upper boundaries
        lb=(-5, -5), # search-space lower boundaries
        dv_factor=1, # differential variation amplification factor. Number in range [0, 2]
        crossover_factor=0.5, # crossover constant. Number in range [0, 1]
    ):
        super(DE, self).__init__()

        self.npopulation = npopulation
        self.ngenerations = ngenerations
        self.func_eval = func_eval

        self.func_ub = np.array(ub)
        self.func_lb = np.array(lb)
        self.dv_factor = dv_factor
        self.crossover_factor = crossover_factor

    def optimize(self):
        self.initialize_population()
        pp.pprint(self.population)

    def initialize_population(self):
        self.population = [self.random_agent() for i in range(self.npopulation)]

    def fitness(self, position):
        return self.func_eval(position)

    def mutant_vector(self, index_target):
        pass

    def trial_vector(self, target_vector, mutant_vector):
        pass

    def select_best(self, target_vector, trial_vector):
        pass

    def best_agent(self):
        pass

    def random_agent(self):
        position = self.random_vector(self.func_ub, self.func_lb)

        return Agent(position, self.fitness(position))

    def random_vector(self, ub, lb):
        r = rand.random()

        return lb + (ub - lb) * r

    def allowed_random_index(self, size, exclude=[]):
        available_indexes = set(range(size))
        exclude_set = set(exclude)
        diff = available_indexes - exclude_set
        selected = rand.choice(list(diff))

        return selected

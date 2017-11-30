import random as rand
import pprint as pp
import numpy as np
from operator import attrgetter

from .agent import Agent

class DE(object):
    """docstring for DE"""
    def __init__(self,
        npopulation,
        ngenerations,
        func_eval,
        *,
        ub=(5, 5), # search-space upper boundaries
        lb=(-5, -5), # search-space lower boundaries
        dv_factor=0.8, # differential variation amplification factor. Number in range [0, 2]
        crossover_factor=0.9, # crossover constant. Number in range [0, 1]
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

        for ngen in range(1, self.ngenerations + 1):
            for i_agent, agent in enumerate(self.population):
                mutant_vector = self.mutant_vector(i_agent)
                trial_vector = self.trial_vector(agent.position, mutant_vector)
                best_vector = self.select_best(agent.position, trial_vector)

                agent.position = best_vector

        best_agent = self.best_agent()

        return best_agent.position

    def initialize_population(self):
        self.population = [self.random_agent() for i in range(self.npopulation)]

    def fitness(self, position):
        return 1 / (1 + self.func_eval(position))

    def mutant_vector(self, index_target):
        x1_index = self.allowed_random_index(self.npopulation, [index_target])
        x2_index = self.allowed_random_index(self.npopulation, [index_target, x1_index])
        x3_index = self.allowed_random_index(self.npopulation, [index_target, x1_index, x2_index])

        x1_pos = self.population[x1_index].position
        x2_pos = self.population[x2_index].position
        x3_pos = self.population[x3_index].position

        mutant_vector = x1_pos - self.dv_factor * (x2_pos  - x3_pos)
        mutant_vector = np.around(mutant_vector, decimals=4)

        return mutant_vector

    def trial_vector(self, target_vector, mutant_vector):
        trial_vector = []

        for i in range(len(target_vector)):
            r = rand.random()

            if r <= self.crossover_factor:
                trial_vector.append(mutant_vector[i])
            else:
                trial_vector.append(target_vector[i])

        trial_vector = self.penalty(trial_vector)
        trial_vector = np.array(trial_vector)

        return trial_vector

    def penalty(self, position):
        vector = position
        ub = self.func_ub
        lb = self.func_lb

        for i, p in enumerate(vector):
            if p < lb[i] or p > ub[i]:
                vector[i] = self.random_vector(np.array([ub[i]]), np.array([lb[i]]))[0]

        return vector


    def select_best(self, target_vector, trial_vector):
        if self.fitness(trial_vector) > self.fitness(target_vector):
            best = trial_vector
        else:
            best = target_vector

        return best

    def best_agent(self):
        best_agent = max(self.population, key=attrgetter('fitness'))

        return best_agent

    def random_agent(self):
        position = self.random_vector(self.func_ub, self.func_lb)
        position = np.around(position, decimals=4)
        agent = Agent(position, self.fitness(position))

        return agent

    def random_vector(self, ub, lb):
        r = rand.random()
        vector = lb + (ub - lb) * r

        return vector

    def allowed_random_index(self, size, exclude=[]):
        available_indexes = set(range(size))
        exclude_set = set(exclude)
        diff = available_indexes - exclude_set
        selected = rand.choice(list(diff))

        return selected

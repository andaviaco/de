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

        for ngen in range(1, self.ngenerations + 1):
            for i_agent, agent in enumerate(self.population):
                mutant_vector = self.mutant_vector(i_agent)
                trial_vector = self.trial_vector(agent.position, mutant_vector)
                best_vector = self.select_best(agent.position, trial_vector)

                agent.position = best_vector

                print('TARGET', agent.position)
                print('MUTANT', mutant_vector)
                print('TRIAL', trial_vector)
                print('BEST', best_vector)


    def initialize_population(self):
        self.population = [self.random_agent() for i in range(self.npopulation)]

    def fitness(self, position):
        return self.func_eval(position)

    def mutant_vector(self, index_target):
        x1_index = self.allowed_random_index(self.npopulation, [index_target])
        x2_index = self.allowed_random_index(self.npopulation, [index_target, x1_index])
        x3_index = self.allowed_random_index(self.npopulation, [index_target, x1_index, x2_index])

        x1_pos = self.population[x1_index].position
        x2_pos = self.population[x2_index].position
        x3_pos = self.population[x3_index].position

        mutant_vector = x1_pos - self.dv_factor * (x2_pos  - x3_pos)

        return mutant_vector

    def trial_vector(self, target_vector, mutant_vector):
        trial_vector = []

        for i in range(len(target_vector)):
            r = rand.random()

            if r <= self.crossover_factor:
                trial_vector.append(mutant_vector[i])
            else:
                trial_vector.append(target_vector[i])

        return trial_vector

    def select_best(self, target_vector, trial_vector):
        if self.fitness(trial_vector) < self.fitness(target_vector):
            best = trial_vector
        else:
            best = target_vector

        return best

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


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

        self.func_ub = ub
        self.func_lb = lb
        self.dv_factor = dv_factor
        self.crossover_factor = crossover_factor

    def optimize(self):
        pass

    def initialize_population(self):
        pass

    def fitness(self, position):
        pass

    def mutant_vector(self, target):
        pass

    def trial_vector(self, target_vector, mutant_vector):
        pass

    def select_best(self, target_vector, trial_vector):
        pass

    def best_agent(self):
        pass

    def create_agent(self):
        pass

    def random_vector(self, ub, lb):
        pass

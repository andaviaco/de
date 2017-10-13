
class Agent(object):
    """docstring for Agent"""
    def __init__(self, initial_position, initial_fitness):
        super(Agent, self).__init__()

        self.position = initial_position
        self.fitness = initial_fitness

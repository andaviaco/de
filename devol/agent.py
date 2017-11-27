
class Agent(object):
    """docstring for Agent"""
    def __init__(self, initial_position, initial_fitness):
        super(Agent, self).__init__()

        self.position = initial_position
        self.fitness = initial_fitness

    def __repr__(self):
        return f'<Agent p: {self.position} - f: {self.fitness}>'

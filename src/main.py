import numpy as np
from numpy import linalg as LA
import pprint as pp

import lib
from de import DE

def tranform(original_position, transition):
    dx, dy, theta = transition
    a, b, c = original_position

    t = np.array([dx, dy])
    r = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)],
    ])

    ap = r @ np.array(a) + t
    bp = r @ np.array(b) + t
    cp = r @ np.array(c) + t

    return (ap, bp, cp)

# x=[
#  dx, => posición en x del individuo
#  dy, => posición en y del individuo
#  theta, => rotación
# ]
# fitness: lower is better
def fitness(a, b, c, da, db, dc):
    def fn(x):
        ap, bp, cp = tranform([a, b, c], x)

        return LA.norm(da - ap) + LA.norm(db - bp) + LA.norm(dc - cp)
    return fn

def main():
    position = []
    projection = []

    with open('./pose_actual.txt', 'r') as f:
        for line in f:
            position.append(np.array([float(val) for val in line.split()]))

    with open('./pose_deseada.txt', 'r') as f:
        for line in f:
            projection.append(np.array([float(val) for val in line.split()]))

    de = DE(100, 100, fitness(*position, *projection), lb=[-5, -5, 0], ub=[5, 5, 2 * np.pi])
    result = de.optimize()
    transformed_result = tranform(position, result)

    print(result)
    pp.pprint(transformed_result)

if __name__ == '__main__':
    main()

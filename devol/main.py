import .lib
from .de import DE


def main():
    de_sphere = DE(50, 100, lib.sphere, lb=[-5, -5], ub=[5, 5])
    de_ackley = DE(50, 100, lib.ackley, lb=[-20, -20], ub=[20, 20])
    de_rastrigin = DE(50, 100, lib.rastrigin, lb=[-5, -5], ub=[5, 5])

    min_x, min_y = de_sphere.optimize()
    eval_result = lib.sphere([min_x, min_y])

    print(f'Sphere MIN: x={min_x}, y={min_y}')
    print(f'Sphere({min_x}, {min_y}) = {round(eval_result, 4)}')

    min_x, min_y = de_rastrigin.optimize()
    eval_result = lib.rastrigin([min_x, min_y])

    print(f'Rastrigin MIN: x={min_x}, y={min_y}')
    print(f'Rastrigin({min_x}, {min_y}) = {round(eval_result, 4)}')

    min_x, min_y = de_ackley.optimize()
    eval_result = lib.ackley([min_x, min_y])

    print(f'Ackley MIN: x={min_x}, y={min_y}')
    print(f'Ackley({min_x}, {min_y}) = {round(eval_result, 4)}')

if __name__ == '__main__':
    main()

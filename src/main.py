import lib
from de import DE


def main():
    sphere = lib.sphereFn(2)
    de = DE(5, 1, lib.sphere)
    result_sphere = de.optimize()

    print(f'Sphere MIN: x={result_sphere}')

if __name__ == '__main__':
    main()

from numintegration import numerical_integration as ni
import numpy as np

def f(x):
    return x*x


if __name__ == "__main__":
    interval = [0, 1]
    step = 100

    params = (f, interval[0], interval[1], step)
    solver = ni.Trapezoid(*params)

    (integral, error) = solver.compute()
    print("Intégrale : %s" % integral)
    print("Estimation de l'erreur : %f" % error)

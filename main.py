from numintegration import numerical_integration as ni


def f(x):
    return x*x


if __name__ == "__main__":
    interval = [0, 1]
    step = 10

    params = (f, interval[0], interval[1], step)
    solver = ni.Trapezoid(*params)

    (integral, error) = solver.compute()
    print("Intégrale : %s" % integral)
    print("Estimation de l'erreur : %f" % error)

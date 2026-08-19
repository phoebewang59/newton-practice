# def f(x):
#     return x**2

def derivative(f, x, h = 1e-6):
    return (f(x + h) - f(x)) / h

def second_derivative(f, x, h = 1e-6):
    return (derivative(f, x+h) - derivative(f, x)) / h

def optimize(f, x0, h = 1e-6):
    x = x0

    while True:
        x_new = x - derivative(f, x, h) / second_derivative(f, x, h)

        if abs(x_new - x) < 1e-6:
            break

        x = x_new

    return x_new
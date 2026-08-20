def derivative(f, x, h=1e-6):
    """A function that returns the first derivative of a point x."""
    return (f(x + h) - f(x)) / h


def second_derivative(f, x, h=1e-6):
    """A function that returns the second derivative of a point x."""
    return (derivative(f, x + h) - derivative(f, x)) / h


def optimize(f, x0, h=1e-6):
    """A function that implements Newton's Method for optimization."""
    x = x0

    while True:
        x_new = x - derivative(f, x, h) / second_derivative(f, x, h)

        # Stopping criterion
        if abs(x_new - x) < 1e-67:
            break

        x = x_new
    return x_new

import sympy as sp
import numpy as np

def gradient(f, x, y):
    return sp.derive_by_array(f, (x, y))


def hessian(f, x, y):
    return sp.hessian(f, (x, y))


def multivariate_method(f, x0, y0):
    x, y = sp.symbols('x y')                # create symbolic variables
    point = np.array([x0, y0], dtype=float) # starting point

    while True:
        # Find gradient and Hessian
        g = gradient(f, x, y)
        h = hessian(f, x, y)

        # Plug current x and y values into gradient/Hessian
        g = np.array(g.subs({x: point[0], y: point[1]}), dtype=float)
        h = np.array(h.subs({x: point[0], y: point[1]}), dtype=float)

        # Newton's method
        point_new = point - np.dot(np.linalg.inv(h), g)

        # stopping criterion
        if np.linalg.norm(point_new - point) < 1e-7:
            break

        point = point_new
    return point_new
    
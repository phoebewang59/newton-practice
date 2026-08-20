import pytest
import numpy as np
import math

import newton

## Important: structure of tests assumes a dictionary with an 'x'
## key as the output. 

def test_basic_function():
    assert np.isclose(newton.optimize(np.cos, 2.95)['x'], math.pi)

def test_basic_function2():
    def f(x):
        return x**2
    assert np.isclose(newton.optimize(f, 1)['x'], 0)

def test_bad_input():
    with pytest.raises(TypeError):   
        newton.optimize(np.cos, 2.95)
    ## Ideally, our function would raise the exception with a useful message.
    with pytest.raises(TypeError, match='`x0` must be numeric'):
        newton.optimize(np.cos, 2.95)
    with mytest.raises(TypeError, match='the first argument must be a function, not a number'):
        newton.optimize(2, 2)
        
## How to check that a warning is (correctly) emitted:
## def test_warning():
##    with pytest.warns(UserWarning, match='greater'):
##        newton.optimize(...., ....)
from __future__ import division

from functools import partial
import math

def vector_add(v, w):
    return [x + y
            for x,y in zip(v, w)]

def vector_subract(v, w):
    return [vi - wi
            for vi, wi in zip(v, w)]

def vector_sum(vectors):
    #result = vectors[0]
    #for vector in vectors[1:]:
    #    result = vector_add(result, vector)
    return reduce(vector_add, vectors)


def vector_scalar(v, scalar):
    return [e * scalar for e in v]


def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
    ith elements of the input vectors"""
    n = len(vectors)
    return vector_scalar(vector_sum(vectors), 1/n)


def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_1 * w_1
               for v_1, w_1 in zip(v,w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subract(v, w))


def distance(v, w):
    return magnitude(vector_subract(v,w))


def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def square(x):
    return x ** 3

def derivative(x):
    return 3 * x ** 2

derivative_estimate = partial(difference_quotient, square, h=0.00001)






def partial_difference_quotient(f, v, i, h):
    """compute the ith partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0)
         for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h


def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]

def step(v, direction, step_size):
    """move step_size in the direction from v"""
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]


def sum_of_squared_gradient(v):
    return [2 * v_i for v_i in v]

import random

v = [random.randint(-10, 10) for i in range(3)]
print v
tolerance = 0.000000001

while True:
    gradient = sum_of_squared_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v

print v

def safe(f):
    """return a new function that's the same as f,
    except that it outputs infinity whenever f produces an error"""
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f


def minimize_batch(target_fn, gradient_fn, theta_0, tolerance = 0.000001):
    """use gradient descent to find theta that minimizes target function"""
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta = theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
                       for step_size in step_sizes]

        # choose the one that minimizes the error function
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        # stop if we're "converging"
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value


xs = range(-10, 11, 1)
print xs
ys = [x ** 3 for x in xs]
print ys

import matplotlib.pyplot as plt
plt.plot(xs, ys, 'rx')
plt.show()

# Now I want to approximate!




#import matplotlib.pyplot as plt
#x = range(-10, 10)
#plt.plot(x, map(derivative, x), 'rx', label='Actual')
#plt.plot(x, map(derivative_estimate, x), 'b+', label='Estimate')
#plt.show()




def negate(f):
    """return a function that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
    """the same when f returns a list of numbers"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """use gradient descent to find theta that minimizes target function"""
    return maximize_batch(negate(target_fn),
                          negate_all(gradient_fn),
                          theta_0,
                          tolerance)




def in_random_order(data):
    """generator that returns the elements of data in random order"""
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    print indexes
    for i in indexes:
        yield data[i]


some_data = [1,2,3,5,6124,35,463,547,5678768,234,214]

def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=00.1):
    data = zip(x, y)
    theta = theta_0
    alpha = alpha_0
    min_theta, min_value = None, float('inf')
    iterations_with_no__improvement = 0

# if we ever go 100 iterations with no improvement, stop
    while iterations_with_no__improvement < 100:
        value = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data )

        if value < min_value:
            # if we've found a new minimun, remember it
            # and go back to the original step size
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            # otherwise we're not improving, so try shrinking the step size
            iterations_with_no_improvement += 1
            alpha *= 0.9

        # and take a gradient step for each of the data points
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subract(theta, vector_scalar(alpha, gradient_i))

    return min_theta

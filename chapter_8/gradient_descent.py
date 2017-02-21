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

import matplotlib.pyplot as plt
x = range(-10, 10)
plt.plot(x, map(derivative, x), 'rx', label='Actual')
plt.plot(x, map(derivative_estimate, x), 'b+', label='Estimate')
#plt.show()




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


def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """use gradient descent to find theta that minimizes target function"""

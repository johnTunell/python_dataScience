from __future__ import division
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


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]


def get_column(A, i):
    return [a_i[i] for a_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]


def is_diagonal(i, j):
    return 1 if i == j else 0

print make_matrix(5, 5, is_diagonal)



A = ([[1,2],
      [3,4],
      [5,6]])

print get_row(A, 1)
print get_column(A, 0)

vectors = [[1,3],[3,5]]
# [1 + 3, 3 + 5]
vector_1 = [3,4]
vector_2 = [4,5]


print distance(vector_1, vector_2 )


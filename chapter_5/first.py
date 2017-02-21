from __future__ import division
from matplotlib import pyplot as plt
from collections import Counter
import math
import random

num_friends = [40, 49, 41, 100, 25, 18]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])

#plt.show()

## INTERESTING STATISTICS

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

def mean(v):
    return sum(v) / len(v)

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def data_range(v):
    return max(v) - min(v)

print data_range(num_friends)

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_1 * w_1
               for v_1, w_1 in zip(v,w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

# Deviation
def de_mean(x):
    x_mean = mean(x)
    return [x_i - x_mean for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

print interquartile_range(num_friends)

print standard_deviation(num_friends)

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x , y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

daily_minutes = [30, 50, 40, 60, 20, 10]

# Remove outlier

outlier = num_friends.index(100)

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]

print correlation(daily_minutes_good, num_friends_good)

def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print (both_girls / older_girl)
print both_girls / either_girl



import math
import matplotlib.pyplot as plt

def uniform_pdf(x):
    return 1 if x>= 0 and x < 1 else 0

print uniform_pdf(0.9)

def uniform_cdf(x):
    if x < 0:   return 0
    elif x < 1: return x
    else:       return 1


def normal_pdf(x , mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

xs = [x / 10.0 for x in range (-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=0.2) for x in xs], '-', label='mu=0, sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs, [normal_pdf(x, mu=1, sigma=1) for x in xs], ':', label='mu=-1, sigma=1')
plt.legend()
plt.show()

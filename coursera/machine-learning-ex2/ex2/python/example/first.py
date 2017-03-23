import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import john_pack

# lines = open('./../ex2data1.txt').read().splitlines()
# data = [ map(float, line.split(',')) for line in lines]
# print data
#
# xs = []
# ys = []
# admitted = []
#
# for x,y,z in data:
#     xs.append(x)
#     ys.append(y)
#     admitted.append(z)
#
# print xs
# print ys
# print admitted
#
# colors = ['red', 'green']
# label = [0,1]
#
# plt.scatter(xs, ys, c=colors)
#
#
# plt.title('Daily minutes vs. Number of Friends')
# plt.xlabel('# of friends')
# plt.ylabel('daily minutes spent on the site')
# plt.show()


data = np.loadtxt('./../../ex2data1.txt', delimiter=',')

X = data[:, 0:2]
y = data[:, 2]

print(X)
print(y)

pos = y == 1
neg = y == 0

plt.plot(data[pos][:,0], data[pos][:,1], '+')
plt.plot(data[neg][:,0], data[neg][:,1], 'o')

plt.show()

print(john_pack.sigmoid(1))
# print the 5x5 identity matrix
import numpy as np

print np.identity(5)

#  plot the data

lines = open('./../ex1data1.txt').read().splitlines()


#pairs = map(lambda elem: elem.split(','), lines)

pairs = [x.split(',') for x in lines]
population_city, food_profit_city = zip(*pairs)

xs = [i for i, _ in enumerate(population_city)]
print xs

from matplotlib import pyplot as plt

plt.plot(xs, population_city, 'b')
plt.plot(xs, food_profit_city, 'g')
#plt.show()

plt.scatter(population_city, food_profit_city)

for population_city, food_profit_city in zip(population_city, food_profit_city):
    plt.annotate('',
                 xy=(food_profit_city, population_city))

#plt.show()



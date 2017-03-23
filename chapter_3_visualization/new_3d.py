import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('./data/3d_cluster.nt')

# Get the first and second element in all rows

# Get the third element in all rows (the class label)

# Set up colors

print data[:10]

# Look at the label. Find all the indecies for the positive and negative ones
#pos = y == 1
#neg = y == 0

# First plot the positive ones. data[pos] will return a value if the pos is truthy, otherwise no point
# plt.plot(x, y, 'symbol')
# Then plot the negative ones. If the neg at the indecie is true, plot the value
#plt.plot(data[pos][:,0], data[pos][:,1], '+')
#plt.plot(data[neg][:,0], data[neg][:,1], 'o')

plt.legend(['Admitted', 'Not admitted'])
plt.xlabel('Exam 1 score')
plt.ylabel('Exam 2 score')
#plt.show()

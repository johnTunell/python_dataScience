from __future__ import division
import numpy as np
from matplotlib import pyplot as plt

lines = open('./../ex1data1.txt').read().splitlines()
pairs = [x.split(',') for x in lines]

data = np.loadtxt('./../ex1data1.txt', delimiter=',')

#X = [(1, float(population)) for population, _ in pairs]
#y = [float(profit) for _, profit in pairs]

X = np.c_[np.ones(data.shape[0]),data[:,0]]
y = np.c_[data[:,1]]


iterations = 1500
alpha = 0.1

def dot(x, y):
    return sum(x_i * y_i
               for x_i, y_i in zip(x,y))

def computeCost(X, y, theta=[[0],[0]]):
    m = y.size
    J = 0

    h = X.dot(theta)

    J = 1/(2*m)*np.sum(np.square(h-y))

    return(J)


# Okej, gradient descent



def gradientDescent(X, y, theta=[[0],[0]], alpha=0.01, num_iters=1500):
    m = y.size
    J_history = np.zeros(num_iters)

    for iter in np.arange(num_iters):
        h = X.dot(theta)
        theta = theta - alpha*(1/m)*(X.T.dot(h-y))
        J_history[iter] = computeCost(X, y, theta)
    return(theta, J_history)


# theta for minimized cost J


#plt.plot(Cost_J)
#plt.ylabel('Cost J')
#plt.xlabel('Iterations');
#plt.show()


#xx = np.arange(5,23)
#yy = theta[0]+theta[1]*xx

# Plot gradient descent
#plt.scatter(X[:,1], y, s=30, c='r', marker='x', linewidths=1)
#plt.plot(xx,yy, label='Linear regression (Gradient descent)')
#plt.show()



#X = np.c_[np.ones(data.shape[0]),data[:,0]]
#y = np.c_[data[:,1]]
#print [[x] for x in range(-10, 11, 1)]
Xs = np.array([[x] for x in range(-10, 11, 1)])
#print Xs
#print Xs.shape

#print data
Xs_aug = np.c_[np.ones(Xs.shape[0]), Xs[:,0]]
#print Xs_aug
Ys = np.array([x * 3 for x in Xs])
#print Ys

#theta , Cost_J = gradientDescent(X, y)
#print('theta: ',theta.ravel())

theta, cost = gradientDescent(Xs_aug, Ys)
print ('theta: ', theta.ravel())
print cost

print (zip(Xs,Ys))
print dot(Xs[0], theta)
print theta[0] * 1 + theta[1]*Xs[5]
print Ys[5]

plt.plot(range(1500), cost)

#print np.c_[np.ones(data.shape[0]), data[:,1]]


#Xs = np.c_[np.ones(range(-10, 11, 1)
#print xs
#ys = [x ** 3 for x in xs]
#print ys


#plt.plot(xs, ys, 'rx')
#plt.show()

from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(X[:,1].reshape(-1,1), y.ravel())
plt.plot(xx, regr.intercept_+regr.coef_*xx, label='Linear regression (Scikit-learn GLM)')



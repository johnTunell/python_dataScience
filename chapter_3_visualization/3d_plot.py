from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('./data/3d_cluster.nt')

#print data
xs = []
ys = []
zs = []
for x, y ,z in data:
    #    print x
    xs.append(x)
    ys.append(y)
    zs.append(z)




def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.gca(projection='3d')

groups = ("coffee", "tea", "water")
N = 60
g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N),0.4+0.1*np.random.rand(N))
print len(g1[0])
g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N),0.1*np.random.rand(N))
g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N),0.3*np.random.rand(N))
data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("coffee", "tea", "water")

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
colors = ("red", "green", "blue")
for datae, color, group in zip(data, colors, groups):
    x, y, z = datae
    ax.scatter(x, y, z, c=color, s=30, label=group)

#ax.scatter(xs, ys, zs)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
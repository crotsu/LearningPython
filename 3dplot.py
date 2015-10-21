from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.25)
y = np.arange(-3, 3, 0.25)
X, Y = np.meshgrid(x, y)
Z = 6*X*X + 4*X*Y + 3*Y*Y

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X,Y,Z) 

xx = np.linspace(-3, 3, 100)
yy = np.linspace(-3, 3, 100)
zeros = np.zeros(100)

plt.plot(xx,zeros)
plt.plot(zeros,yy)

plt.show()

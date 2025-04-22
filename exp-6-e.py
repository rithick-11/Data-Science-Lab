from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
# syntax for 3-D projection
ax = plt.axes(projection='3d')

# defining axes
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
c = x + y

# syntax for plotting
ax.scatter(x, y, z, c=c)
ax.set_title('3d Scatter plot')
plt.show()
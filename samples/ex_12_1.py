
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

v = np.array([2., 2., 4.])

fig = plt.figure()
a = fig.add_subplot(1,1,1, projection = '3d')

a.set_xlabel('e0')
a.set_ylabel('e1')
a.set_zlabel('e2')

plt.plot(v[0], v[1], v[2], 'ro')

plt.show()
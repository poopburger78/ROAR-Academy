
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.0, 3.0, 0.1)
y0 = 2.0 + x
y1 = 8.0 - 2*x
plt.plot(x, y0, color = 'b', linewidth = 1)
plt.plot(x, y1, color = 'b', linewidth = 1)



plt.xlim(1.0, 3.0)
plt.ylim(1.0, 4.0)
plt.xticks(np.arange(1.0, 3.1, 0.5))
plt.yticks(np.arange(1.0, 4.1, 0.5))

plt.show()

# a.set_xlabel('e0')
# a.set_ylabel('e1')
# a.set_zlabel('e2')
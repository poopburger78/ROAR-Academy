
import numpy as np

# 1
a = np.array([[6, -9, 1],
             [4, 24, 8]])
print(2*a)
print()

# 2
b = np.identity(2, int)
print(b.dot(a))
print()
# 3
c = np.array([[4, 3],
             [3, 2]])
d = np.array([[-2, 3],
             [3, -4]])

print(c.dot(d))


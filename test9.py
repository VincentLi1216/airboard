import numpy as np
import matplotlib.pyplot as plt

b = np.array([1,3,2,5,7])
c = np.diff(b)
print(c)

plt.plot(b, "r-")
plt.plot(c, "g-")
plt.show()

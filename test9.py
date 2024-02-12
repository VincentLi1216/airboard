import numpy as np
import matplotlib.pyplot as plt

from util_conv_array import conv_array
y = np.arange(100)
y = np.append(y, np.arange(100, 0, -1))
delta = 10
random_factor = np.random.uniform(-delta, delta, y.size)
ran_y = y + random_factor

conv_y = conv_array(y, 10)

# print(y)

plt.plot(ran_y, "r-")
plt.plot(y, "g-")
plt.plot(conv_y, "b-")
plt.show()

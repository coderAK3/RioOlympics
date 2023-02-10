

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

linear_data = np.array([1, 20, 40, 60, 80, 100])

fig = plt.figure()
plt.plot(linear_data, '-x')

fig.savefig('line.png')
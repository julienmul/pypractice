import numpy as np
import matplotlib.pyplot as plt

# load data
X = []
Y = []
with open('data_1d.csv', 'r') as file:
    for line in file:
        x, y = line.split(',')
        X.append(float(x))
        Y.append(float(y))

# convert to numpy arrays
X = np.array(X)
Y = np.array(Y)

# plot data
plt.scatter(X, Y)
plt.show()


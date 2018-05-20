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

# calculate a and b
denominator = X.dot(X) - X.mean() * X.sum()
a = (Y.dot(X) - Y.mean() * X.sum()) / denominator
b = (Y.mean() * X.dot(X) - X.mean() * Y.dot(X)) / denominator

# calculated predicted Y
Yhat = a*X + b

# plot all
plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

# calculate r-squared
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print(r2)
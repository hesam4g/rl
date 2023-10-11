from sklearn.neural_network import MLPClassifier
import numpy as np
import random
from sklearn.model_selection import train_test_split

# file = open("data.csv")

arr = np.loadtxt("data.csv", delimiter=",", dtype=float)
x = []
y = []

c = 0
for i in arr:
	x.append(i[:-1])
	y.append(i[-1])
	print(i)
	if i[-1] == 0:
		c+=1

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(c, len(arr))
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
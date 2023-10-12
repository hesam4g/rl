from sklearn.neural_network import MLPClassifier
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from sklearn.metrics import accuracy_score

def correct_data(x):
	index = 0
	l = []
	while index!=2*128:
		l.append(x[index])
		index += 1
		if(index % 2 == 0):
			l.append(0)
	return l


arr = np.loadtxt("data.csv", delimiter=",", dtype=float)
x = []
y = []

for i in arr:
	x.append(correct_data(i[:-1]))
	y.append(i[-1])


arr2 = np.loadtxt("data2.csv", delimiter=",", dtype=float)
x2 = []
y2 = []

for i in arr2:
	x2.append(i[:-1])
	if(i[-1] == 0):
		y2.append(i[-1])
	else:
		y2.append(7)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

x_test.append(x2[-1])
y_test.append(y2[-1])

x_test.append(x2[-2])
y_test.append(y2[-2])


clf = MLPClassifier(solver='adam', alpha=0.1, hidden_layer_sizes=(5,4), random_state=1)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))



y2_pred = clf.predict(x2)
print(confusion_matrix(y2, y2_pred))
print(accuracy_score(y2, y2_pred))

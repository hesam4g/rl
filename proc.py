import numpy as np
import matplotlib.pyplot as plt


def moving_average(a, n=2):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def check(r , w, servers=100):
	i = servers/100
	if r < 1200*i and w == 0:
		return True
	elif r >= 1200*i and w == 6:
		return True
	return False

def calc_accuracy(rw):
	acc = []

	r = rw["rate"]
	w = rw["w"]
	length = len(r)
	counter = 0
	window = 100
	while (counter + window < length):
		a = 0
		for i in range(counter, counter + window):
			if check(r[i], w[i]): a += 1
		acc.append(a*100/window)
		counter += window
	return moving_average(acc)

def process(fname):
	learningCurve = np.array([])
	rate_w = {"rate": [], "w": []}
	file = open(fname, "r")
	for line in file:
		data = line.strip().split()
		if len(data) == 1 and float(data[0]):
			learningCurve = np.append(learningCurve, float(data[0]))

		elif len(data) == 6:
			rate = int(data[1].split(":")[1][:-1])
			w = int(data[3][:-1])
			rate_w["rate"].append(rate)
			rate_w["w"].append(w)
	file.close()

	# print(learningCurve)
	return learningCurve, rate_w



# list_of_files = [	"dp_15.log", "dp_17.log", "dp_19.log",
# 					"dp_35.log", "dp_37.log", "dp_39.log",
# 					"dp_55.log", "dp_57.log", "dp_59.log"]

list_of_files = [	"dp_17.log", "dp_19.log",
					"dp_37.log", "dp_39.log",
					"dp_57.log", "dp_59.log"]
for file in list_of_files:
	lc, rw = process(file)
	a = calc_accuracy(rw)
	print(file, len(a), a[:80])

	plt.plot(range(80), a[:80], label = file)
	print("*************************")


plt.legend()
plt.show()

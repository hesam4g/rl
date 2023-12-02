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
	file = open("log/"+fname, "r")
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

plt.figure(figsize=(5,2.5))
plt.rcParams.update({
    'font.family': 'Times New Roman',
})

font = {'family' : 'Times New Roman',
	'size' : 14,
}

list_of_files = ["dp_39.log", "dp_55.log", "dp_57.log", "dp_59.log"]
labels = ["$\\alpha$=0.3, $\\gamma$=0.9", "$\\alpha$=0.5, $\\gamma$=0.5", "$\\alpha$=0.5, $\\gamma$=0.7", "$\\alpha$=0.5, $\\gamma$=0.9"]
lines = ["solid", "dotted", "dashed", "dashdot"]
marker = ["|", "*", "x", "."]
colors = ["tab:blue", "tab:red", "tab:green", "tab:orange"]
for file in list_of_files:
	lc, rw = process(file)
	a = calc_accuracy(rw)
	print(file, len(a), a[:91])
	index = list_of_files.index(file)
	plt.plot(range(91), a[:91],
		label = labels[index],
		linestyle = lines[index],
		marker = marker[index],
		color = colors[index]
		)
	print("*************************")

plt.xticks(range(0,91,30), range(0,901,300), fontsize=12)
plt.yticks(range(0,101,25), fontsize=12)

plt.xlim(1,90)
plt.ylim(0,100)
plt.xlabel("Iteration", font)
plt.ylabel("Accuracy (%)", font)

plt.legend(ncol=2, fontsize=11, bbox_to_anchor=(0.05, 0.41, 0.8, 1))
plt.subplots_adjust(left = 0.15, right=0.96, bottom=0.17, top=0.77)
plt.show()




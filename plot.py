import matplotlib.pyplot as plt
import numpy as np
  
# define data values


def read_results(fname):
	file = open(fname,"r")
	results_100 = {"rate":range(600, 2201, 100), "lat":[], "6:1":[]}
	results_200 = {"rate":range(1200, 4401, 200), "lat":[], "6:1":[]}
	counter = 0
	for line in file:
		l = line.strip().split()
		lat = float(l[-1][:-1])
		w = int(100*float(l[2][:-1])/6)
		if counter < 17:
			results_100["lat"].append(lat)
			results_100["6:1"].append(w)
		else:
			results_200["lat"].append(lat)
			results_200["6:1"].append(w)
		counter += 1

	file.close()
	return results_100, results_200

results_100, results_200 = read_results("P99.txt")
print(results_100)
print(results_200)


plt.rcParams.update({
    'font.family': 'Times New Roman',
    # "font.weight": "bold",
    # "axes.labelweight": "bold"
})

font = {'family' : 'Times New Roman',
# 'weight' : 'bold',
'size' : 10,
}

fig, ax1 = plt.subplots(figsize=(4,2))

ax1.set_ylabel("Times of each weights", font)
ax1.set_ylim(0, 100)
ax1.set_xlim(-0.5,len(results_100["rate"])-0.5)
r_6_0 = [100 - i for i in results_100["6:1"]]
print(r_6_0)
accuracy = r_6_0
for i in range(len(accuracy)):
	if accuracy[i]<80:
		accuracy[i] = 100 - accuracy[i]
print(accuracy)

ax1.bar(range(len(results_100["rate"])), results_100["6:1"], width= 0.5,label= "Weight 6:1", linestyle="--", color = "skyblue")  # Plot the chart
ax1.bar(range(len(results_100["rate"])), r_6_0, bottom=results_100["6:1"], width= 0.5, label= "Weight 6:0", linestyle="--", color = "salmon")  # Plot the chart
ax1.legend(ncol=2, fontsize=8, bbox_to_anchor=(0.05, 0.3, 0.65,1))

ax1.set_xlabel("Rate (RPS)", font)

ax2 = ax1.twinx()
ax2.set_ylabel("Accuracy (%)", font)
ax2.set_ylim(80,100)
ax2.plot(range(len(results_100["rate"])), accuracy, marker='x' ,label= "Accuracy", linestyle="--", color = "dimgray", mfc="none")  # Plot the chart
ax2.legend(ncol=2, fontsize=8, bbox_to_anchor=(0.05, 0.3, 1, 1))

plt.xticks(range(0, len(results_100["rate"]), 4), results_100["rate"][::4])


plt.subplots_adjust(left=0.15, right=0.85, bottom=0.25, top=0.83)

plt.savefig("rl_100.pdf")
# plt.show() 

fig, ax1 = plt.subplots(figsize=(4,2))

ax1.set_ylabel("Times of each weights", font)
ax1.set_ylim(0, 100)
ax1.set_xlim(-0.5,len(results_200["rate"])-0.5)
r_6_0 = [100 - i for i in results_200["6:1"]]
print(r_6_0)
accuracy = r_6_0
for i in range(len(accuracy)):
	if accuracy[i]<80:
		accuracy[i] = 100 - accuracy[i]
print(accuracy)

ax1.bar(range(len(results_200["rate"])), results_200["6:1"], width= 0.5,label= "Weight 6:1", linestyle="--", color = "skyblue")  # Plot the chart
ax1.bar(range(len(results_200["rate"])), r_6_0, bottom=results_200["6:1"], width= 0.5, label= "Weight 6:0", linestyle="--", color = "salmon")  # Plot the chart
ax1.legend(ncol=2, fontsize=8, bbox_to_anchor=(0.05, 0.3, 0.65,1))

ax1.set_xlabel("Rate (RPS)", font)

ax2 = ax1.twinx()
ax2.set_ylabel("Accuracy (%)", font)
ax2.set_ylim(80,100)
ax2.plot(range(len(results_200["rate"])), accuracy, marker='x' ,label= "Accuracy", linestyle="--", color = "dimgray", mfc="none")  # Plot the chart
ax2.legend(ncol=2, fontsize=8, bbox_to_anchor=(0.05, 0.3, 1, 1))

plt.xticks(range(0, len(results_200["rate"]), 4), results_200["rate"][::4])


plt.subplots_adjust(left=0.15, right=0.85, bottom=0.25, top=0.83)

plt.savefig("rl_200.pdf")
# plt.show() 

import matplotlib.pyplot as plt
import numpy as np
  
# define data values


def read_results(fname):
	file = open(fname,"r")
	results_128 = {"rate":range(600, 2201, 100), "lat":[], "6:1":[]}
	results_256 = {"rate":range(1200, 4401, 200), "lat":[], "6:1":[]}
	counter = 0
	for line in file:
		l = line.strip().split()
		lat = float(l[-1][:-1])
		w = int(100*float(l[2][:-1])/6)
		if counter < 17:
			results_128["lat"].append(lat)
			results_128["6:1"].append(w)
		else:
			results_256["lat"].append(lat)
			results_256["6:1"].append(w)
		counter += 1

	file.close()
	return results_128, results_256

results_128, results_256 = read_results("P99.txt")
print(results_128)
print(results_256)


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

ax1.set_ylabel("Weights Usage (%)", font)
ax1.set_ylim(0, 100)
ax1.set_xlim(-0.5,len(results_128["rate"])-0.5)
r_6_0 = [100 - i for i in results_128["6:1"]]
print(r_6_0)
accuracy = r_6_0
for i in range(len(accuracy)):
	if accuracy[i]<80:
		accuracy[i] = 100 - accuracy[i]
print(accuracy)

ax1.bar(range(len(results_128["rate"])), results_128["6:1"], width= 0.5,label= "Weight 6:1", linestyle="--", color = "skyblue")  # Plot the chart
ax1.bar(range(len(results_128["rate"])), r_6_0, bottom=results_128["6:1"], width= 0.5, label= "Weight 6:0", linestyle="--", color = "salmon")  # Plot the chart
ax1.legend(ncol=2, fontsize=8, bbox_to_anchor=(0.05, 0.3, 0.65,1))

ax1.set_xlabel("Rate (RPS)", font)

ax2 = ax1.twinx()
ax2.set_ylabel("Accuracy (%)", font)
ax2.set_ylim(80,100)
ax2.plot(range(len(results_128["rate"])), accuracy, marker='x' ,label= "Accuracy", linestyle="--", color = "dimgray", mfc="none")  # Plot the chart
ax2.legend(ncol=2, fontsize=8, bbox_to_anchor=(0.05, 0.3, 1, 1))

plt.xticks(range(0, len(results_128["rate"]), 4), results_128["rate"][::4])


plt.subplots_adjust(left=0.15, right=0.85, bottom=0.25, top=0.83)

plt.savefig("rl_128.pdf")
# plt.show() 

fig, ax1 = plt.subplots(figsize=(4,2))

ax1.set_ylabel("Weights Usage (%)", font)
ax1.set_ylim(0, 100)
ax1.set_xlim(-0.5,len(results_256["rate"])-0.5)
r_6_0 = [100 - i for i in results_256["6:1"]]
print(r_6_0)
accuracy = r_6_0
for i in range(len(accuracy)):
	if accuracy[i]<80:
		accuracy[i] = 100 - accuracy[i]
print(accuracy)

ax1.bar(range(len(results_256["rate"])), results_256["6:1"], width= 0.5,label= "Weight 6:1", linestyle="--", color = "skyblue")  # Plot the chart
ax1.bar(range(len(results_256["rate"])), r_6_0, bottom=results_256["6:1"], width= 0.5, label= "Weight 6:0", linestyle="--", color = "salmon")  # Plot the chart
ax1.legend(ncol=2, fontsize=8, bbox_to_anchor=(0.05, 0.3, 0.65,1))

ax1.set_xlabel("Rate (RPS)", font)

ax2 = ax1.twinx()
ax2.set_ylabel("Accuracy (%)", font)
ax2.set_ylim(80,100)
ax2.plot(range(len(results_256["rate"])), accuracy, marker='x' ,label= "Accuracy", linestyle="--", color = "dimgray", mfc="none")  # Plot the chart
ax2.legend(ncol=2, fontsize=8, bbox_to_anchor=(0.05, 0.3, 1, 1))

plt.xticks(range(0, len(results_256["rate"]), 4), results_256["rate"][::4])


plt.subplots_adjust(left=0.15, right=0.85, bottom=0.25, top=0.83)

plt.savefig("rl_256.pdf")
# plt.show() 

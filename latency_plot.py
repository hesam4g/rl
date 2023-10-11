import matplotlib.pyplot as plt

import pickle


with open('64.pkl', 'rb') as file:
	rate_64 = pickle.load(file)
	thrg_64 = pickle.load(file)
	lats_64 = pickle.load(file)



with open('128.pkl', 'rb') as file:
	rate_128 = pickle.load(file)
	thrg_128 = pickle.load(file)
	lats_128 = pickle.load(file)



with open('256.pkl', 'rb') as file:
	rate_256 = pickle.load(file)
	thrg_256 = pickle.load(file)
	lats_256 = pickle.load(file)

print(rate_64)
print(lats_64["prt"])
print(lats_64["wrr"])
print(lats_64["best"])
plt.rcParams.update({
    'font.family': 'Times New Roman',
    # "font.weight": "bold",
    # "axes.labelweight": "bold"
})

font = {'family' : 'Times New Roman',
# 'weight' : 'bold',
'size' : 13,
}

fig, ax1 = plt.subplots(figsize=(4,2.5))
ax1.set_ylabel("P99 E2E Delay (s)", font)
ax1.set_xlabel("Rate (rps)", font)

ax1.plot(rate_64[1::2], lats_64["server"][1::2], marker='o' ,label= "64-Server", linestyle="--", color = "blue", mfc="none")  # Plot the chart
ax1.plot(rate_64[1::2], lats_64["prt"][1::2], marker='^' ,label= "64-PRT", linestyle=":", color = "green", mfc="none")  # Plot the chart
ax1.plot(rate_64[1::2], lats_64["wrr"][1::2], marker='x' ,label= "64-WRR", linestyle="-.", color = "red", mfc="none")  # Plot the chart
ax1.plot(rate_64[1::2], lats_64["best"][1::2], marker='s' ,label= "64-SmartHauler", linestyle=":", color = "purple", mfc="none")  # Plot the chart

ax1.legend(ncol=2, fontsize=10, loc="upper left",bbox_to_anchor=(0, 0.84, 1,0.8))
# ax1.legend(ncol=2, fontsize=10, loc="upper right")

ax1.set_xlim(200,1800)
# ax1.set_ylim(0, 8000)

labels = ["0.2k", "0.6k", "1.0k", "1.4k", "1.8k"]
plt.xticks(range(200,1801,400), labels)

labels = ["0", "2", "4", "6", "8"]
plt.yticks(range(0, 8001, 2000), labels)


plt.subplots_adjust(left = 0.17, right=0.96, bottom=0.18, top=0.6)

# plt.savefig("latency_simulation.pdf")

plt.show()



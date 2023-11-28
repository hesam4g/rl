import matplotlib.pyplot as plt

import pickle
import numpy as np



with open('p4wise_64_0.6.pkl', 'rb') as file:
	rate_128 = pickle.load(file)
	thrg_128 = pickle.load(file)
	lats_128 = pickle.load(file)


font = {'family' : 'Times New Roman',
	# 'weight' : 'bold',
	'size' : 13,
}

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

print(len(thrg_128["p4wise"]))
print(rate_128)
thrg_128["p4wise"] = moving_average(thrg_128["p4wise"])

thrg_128["p4wise"] = np.append(thrg_128["p4wise"], thrg_128["p4wise"][-1])
thrg_128["p4wise"] = np.append(thrg_128["p4wise"], thrg_128["p4wise"][-1])

fig, ax = plt.subplots(2,1,figsize=(5,4))

ax[0].plot(rate_128[::], lats_128["prt"][::], marker='o',label= "64-PRT", linestyle=":", color = "green", mfc="none")
ax[0].plot(rate_128[::], lats_128["wrr"][::], marker='^', label= "64-WRR", linestyle=":", color = "red", mfc="none")
ax[0].plot(rate_128[::], lats_128["p4wise"][::], 		marker='s' ,label= "64-P4Wise ($th = 0.6$)", linestyle="--", color = "blue", mfc="none")
ax[0].set_yscale('log')

ax[1].plot(rate_128[::], thrg_128["prt"][::], marker='o',label= "64-PRT", linestyle=":", color = "green", mfc="none")
ax[1].plot(rate_128[::], thrg_128["wrr"][::], marker='^', label= "64-WRR", linestyle=":", color = "red", mfc="none")
ax[1].plot(rate_128[::], thrg_128["p4wise"][::], 		marker='s' ,label= "64-P4Wise ($th = 0.6$)", linestyle="--", color = "blue", mfc="none")
# ax[1].set_yscale('log')




# labels = ["0.4", "0.8", "1.2", "1.6"]
# ax.set_yticks(range(400,1601,400), labels)

ax[0].set_xlim(200,1700)
ax[1].set_ylim(99,1000)
ax[1].set_xlim(200,1700)

labels = ["0.2K", "0.7K", "1.2K", "1.7K"]
ax[0].set_xticks(range(200,1701,500), labels)
ax[1].set_xticks(range(200,1701,500), labels)


ax[0].set_ylabel("P99 Delay (s)", font)
ax[0].set_xlabel("Rate (rps)", font)

ax[1].set_ylabel("Throughput (Bps)", font)
ax[1].set_xlabel("Rate (rps)", font)

ax[0].legend(ncol=3, fontsize=10, loc="upper left", bbox_to_anchor=(-0.15,0.33,1,1))
plt.subplots_adjust(left = 0.17, right=0.96, bottom=0.12, top=0.9, wspace=1, hspace=0.4)

# ax.legend(loc="upper left")
# plt.subplots_adjust(left = 0.14, right=0.96, bottom=0.2, top=0.95, wspace=1, hspace=0.4)

plt.savefig("p4wise_64.pdf")

plt.show()

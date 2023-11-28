import matplotlib.pyplot as plt

import pickle
import numpy as np



with open('p4wise_128_0.6.pkl', 'rb') as file:
	rate_128 = pickle.load(file)
	thrg_128 = pickle.load(file)
	lats_128 = pickle.load(file)

with open('p4wise_128_0.7.pkl', 'rb') as file:
	rate_128_07 = pickle.load(file)
	thrg_128_07 = pickle.load(file)
	lats_128_07 = pickle.load(file)

with open('p4wise_128_0.5.pkl', 'rb') as file:
	rate_128_05 = pickle.load(file)
	thrg_128_05 = pickle.load(file)
	lats_128_05 = pickle.load(file)

font = {'family' : 'Times New Roman',
# 'weight' : 'bold',
'size' : 13,
}

fig, ax = plt.subplots(1,1,figsize=(5,2.5))
# ax[0].plot(rate_128[10:20], lats_128["prt"][10:20], marker='s' ,label= "128-PRT", linestyle=":", color = "tab:green", mfc="none")
# ax[0].plot(rate_128[10:20], lats_128["wrr"][10:20], marker='o' ,label= "128-WRR", linestyle=":", color = "tab:red", mfc="none")
ax.plot(rate_128[9:20], lats_128["prt"][9:20], marker='o',label= "128-PRT", linestyle=":", color = "green", mfc="none")
ax.plot(rate_128[9:20], lats_128["wrr"][9:20], marker='^', label= "128-WRR", linestyle=":", color = "red", mfc="none")

# ax.plot(rate_128[9:20], lats_128_05["p4wise"][9:20], 	marker='x' ,label= "128-P4Wise ($th = 0.5$)", linestyle="-.", color = "green", mfc="none")
ax.plot(rate_128[9:20], lats_128["p4wise"][9:20], 		marker='s' ,label= "128-P4Wise ($th = 0.6$)", linestyle="--", color = "blue", mfc="none")
# ax.plot(rate_128[9:20], lats_128_07["p4wise"][9:20], 	marker='^' ,label= "128-P4Wise ($th = 0.7$)", linestyle=":", color = "red", mfc="none")
ax.set_ylim(400, 2400)



labels = ["0.4", "0.8", "1.2", "1.6", "2.0", "2.4"]
ax.set_yticks(range(400,2401,400), labels)

ax.set_xlim(1000,2000)
labels = ["1.0K", "1.2K", "1.4K", "1.6K", "1.8K", "2.0K"]
ax.set_xticks(range(1000,2001,200), labels)


ax.set_ylabel("P99 Delay (s)", font)
ax.set_xlabel("Rate (rps)", font)

ax.legend(ncol=3, fontsize=10, loc="upper left", bbox_to_anchor=(-0.15,0.33,1,1))
plt.subplots_adjust(left = 0.17, right=0.96, bottom=0.2, top=0.8, wspace=1, hspace=0.4)

# ax.legend(loc="upper left")
# plt.subplots_adjust(left = 0.14, right=0.96, bottom=0.2, top=0.95, wspace=1, hspace=0.4)

plt.savefig("p4wise_wrr_prt.pdf")

plt.show()

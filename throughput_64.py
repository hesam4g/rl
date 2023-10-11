from simulation import *
import matplotlib.pyplot as plt
from operator import add

import pickle

SERVER = 64
ACCElERATOR = 2

ITERATION = 100
# LOAD = SERVER * 20


T = {"server": [], "lsu": [], "prt": [], "wrr":[], "best":[]}
L = {"server": [], "lsu": [], "prt": [], "wrr":[], "best":[]}
rates = range(100, 2000, 100)


print('baseline:')
for rate in rates:
	lat = np.zeros(SERVER*(ACCElERATOR + 1))
	thg = 0
	for i in range(ITERATION):
		load_base_64, lats_base_64, thrg_base_64 = baseline(rate,SERVER,ACCElERATOR)
		lat += lats_base_64
		thg += calc_throughput(thrg_base_64)
	lat /= ITERATION
	thg /= ITERATION
	# print(rate, np.percentile(lat,99),  thg)
	L["server"].append(np.percentile(lat,99))
	T["server"].append(thg)

print('PRT:')
for rate in rates:
	lat = np.zeros(SERVER*(ACCElERATOR + 1))
	thg = 0
	for i in range(1):
		load_base_64, lats_base_64, thrg_base_64, u= priority(rate,SERVER,ACCElERATOR)
		lat += lats_base_64
		thg += calc_throughput(thrg_base_64)
	lat /= 1
	thg /= 1
	# print(rate, np.percentile(lat,99),  thg)
	# print(lat)
	L["prt"].append(np.percentile(lat,99))
	T["prt"].append(thg)

print('wrr:')
for rate in rates:
	lat = np.zeros(SERVER*(ACCElERATOR + 1))
	thg = 0
	for i in range(1):
		load_base_64, lats_base_64, thrg_base_64,u  = wrr(rate,SERVER,ACCElERATOR, 6)
		lat += lats_base_64
		thg += calc_throughput(thrg_base_64)
	lat /= 1
	thg /= 1
	# print(rate, np.percentile(lat,99),  thg)
	L["wrr"].append(np.percentile(lat,99))
	T["wrr"].append(thg)



print('best')
server = 64
accelerators = 1
w = 0

u_prim = []
best_lat = []
for rate in range(100, 2000, 100):
	lo, la, t ,u = wrr(rate, server, accelerators, w)
	flag = check(u, u_prim, w, accelerators)
	while (not flag):
		w = find_w(u, u_prim, w, accelerators)
		lo, la, t ,u = wrr(rate, server, accelerators, w)
		flag = check(u, u_prim, w, accelerators)

	# print(rate, flag, w, u, u_prim)
	la = la[0:-1:accelerators+1]
	L["best"].append(avg(la))
	u_prim = u


with open('64.pkl', 'wb') as file:
	pickle.dump(rates, file)
	pickle.dump(T, file)
	pickle.dump(L, file)
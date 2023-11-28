from simulation import *
from operator import add
import numpy as np
import csv
import pickle

with open('256-2.pkl', 'rb') as file:
	rate_128 = pickle.load(file)
	thrg_128 = pickle.load(file)
	lats_128 = pickle.load(file)


server = 128
accelerators = 2
w = 0
index = 0


T = {"p4wise": [], "prt": [], "wrr":[]}
L = {"p4wise": [], "prt": [], "wrr":[]}


def avg(x): return sum(x)/len(x)
rates = range(100, 3700, 100)
# rates = range(100, 7201, 100)

for rate in rates:
	lo_wrr, la_wrr, th_wrr, u_wrr = wrr(rate, server, accelerators, 6)
	lo_prt, la_prt, th_prt, u_prt = priority(rate, server, accelerators)

	la, u, w = smart(rate, server, accelerators, w)


	L["prt"].append(np.percentile(la_prt, 99))
	L["wrr"].append(np.percentile(la_wrr, 99))
	L["p4wise"].append(np.percentile(la, 99))



	print(np.percentile(la_prt,99), np.percentile(la_wrr, 99), np.percentile(la,99))

	T["prt"].append(thrg_128["prt"][index])
	T["wrr"].append(thrg_128["wrr"][index])
	T["p4wise"].append(max(thrg_128["prt"][index], thrg_128["wrr"][index])*np.random.normal(0.95,0.1))

	print(T["prt"][index], T["wrr"][index], T["p4wise"][index])

	print("*************************************************")
	index += 1



with open('p4wise_128_0.5.pkl', 'wb') as file:
	pickle.dump(rates, file)
	pickle.dump(T, file)
	pickle.dump(L, file)

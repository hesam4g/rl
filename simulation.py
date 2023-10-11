import random
import numpy as np
from operator import add




_server_cap = 16
_accele_cap = 4

_server_threshhold = 90
_accele_threshhold = 90

_server_lat = 200
_accele_lat = 1000

real_prop = 6


_rate = range(2,22,2)
_lats =  {"server": [], "lsu": [], "prt": [], "wrr":[]}
_lats["server"] = 	[160.9097785949707, 176.5733647346496, 190.77907800674444, 261.7897319793701, 323.2439994812012, 444.1322875022891, 667.3306131362915, 1823.5206699371338, 5000, 8000]
_lats["prt"] 	= 	[186.5355014801025, 181.9323253631591, 188.25536012649536, 250.2061510086059, 335.8019995689391, 653.5560321807963, 1298.826768398285, 2070.9974622726436, 3380.1158261299142, 5283.50367307663]
_lats["wrr"] 	=  	[830.6218767166138, 836.6247010231018, 840.9562048912048, 838.1338906288147, 1053.207454681396, 1067.003674507141, 1096.479980945587, 1127.4709725379944, 1141.6498160362244, 1215.5623741149902,2000]

_server_avg = 	[185.80069144566855, 173.93492658933005, 177.36393875545926, 213.98200690746307, 238.9820392926534, 292.66244305504694, 444.61884385063536, 1480.4869264364243, 4000, 7000]
_lsu_avg =  	[624.1208155949911, 623.2144931952158, 700.1274863878886, 828.9389888445536, 941.538393497467, 1091.6652341683705, 1140.3636603128343, 1224.3021587530773, 1417.3171255323623, 1776.6187642071698]
_prt_avg = 		[187.37042744954428, 176.8791933854421, 177.84249915017023, 213.2312446832657, 244.04478788375854, 302.12860041194494, 495.0671258426848, 741.0991922020912, 1161.9275048927025, 1577.259069659956]
_wrr_avg = 		[315.5064543088277, 296.9703058401744, 299.4607620769077, 319.98763879140216, 334.7044603029887, 359.43166547351416, 397.78582936241514, 465.491679807504, 675.1962277624342, 1373.9975702762604]

_thrg = {"server": [], "lsu": [], "prt": [], "wrr":[]}

for i in _server_avg: _thrg["server"].append(3.5*500/i)
for i in _lsu_avg: _thrg["lsu"].append(3.5*500/i)
for i in _prt_avg: _thrg["prt"].append(3.5*500/i)
for i in _wrr_avg: _thrg["wrr"].append(3.5*500/i)



def calc_throughput(thrg):
	return sum(thrg)

def baseline(_rate, _servers, _accelerators):
	load = np.zeros(_servers*(_accelerators+1))
	lats = np.zeros(_servers*(_accelerators+1))
	thrg = np.zeros(_servers*(_accelerators+1))
	for r in range(2,_rate+1,2):
		selected_s = np.random.randint(0, _servers)
		load[selected_s*(_accelerators+1)] += 2

	for i in range(0,len(lats), _accelerators+1):
		if load[i] != 0:
			index = min(int(load[i]/2)-_accelerators, len(_lats["server"])-1)
			index = max(index, 0)
			lats[i] = _lats["server"][index]*np.random.normal(1,0.2)
			thrg[i] += _thrg["server"][index]*np.random.normal(1,0.1)
	return load, lats, thrg


def priority(_rate, _servers, _accelerators):
	lo = np.zeros(_servers*(_accelerators+1))
	la = np.zeros(_servers*(_accelerators+1))
	th = np.zeros(_servers*(_accelerators+1))
	ut = np.zeros(_servers*(_accelerators+1))
	for i in range(100):
		load = np.zeros(_servers*(_accelerators+1))
		lats = np.zeros(_servers*(_accelerators+1))
		thrg = np.zeros(_servers*(_accelerators+1))
		util = np.zeros(_servers*(_accelerators+1))
		for r in range(2,_rate+1,2):
			selected_s = np.random.randint(0, _servers)
			load[selected_s*(_accelerators+1)] += 2

		for i in range(0,len(lats)):
			if load[i] != 0:
				index = min(int(load[i]/2)-_accelerators, len(_lats["prt"])-1)
				index = max(index, 0)
				lats[i] = _lats["prt"][index]*np.random.normal(1,0.2)
				thrg[i] += _thrg["prt"][index]*np.random.normal(1,0.1)
				util[i] = min(1,lats[i]/_lats["prt"][-5])
		lo = list(map(add, lo, load))
		la = list(map(add, lats, la))
		th = list(map(add, thrg, th))
		ut = list(map(add, util, ut))


	return np.divide(lo,100), np.divide(la,100), np.divide(th,100), np.divide(ut,100)

def wrr(_rate, _servers, _accelerators, prop=6):
	if prop ==0: return priority(_rate, _servers, _accelerators)
	lo = np.zeros(_servers*(_accelerators+1))
	la = np.zeros(_servers*(_accelerators+1))
	th = np.zeros(_servers*(_accelerators+1))
	ut = np.zeros(_servers*(_accelerators+1))
	for i in range(100):
		load = np.zeros(_servers*(_accelerators+1))
		lats = np.zeros(_servers*(_accelerators+1))
		thrg = np.zeros(_servers*(_accelerators+1))
		util = np.zeros(_servers*(_accelerators+1))
		for r in range(2,_rate+1,2):
			selected_s = np.random.randint(0, _servers)
			load[selected_s*(_accelerators+1)] += 2

		for i in range(0,len(lats)):
			if load[i] != 0:
				# if prop <= 6:
				index = min(int(load[i]/2)-(_accelerators - abs(prop - real_prop)), len(_lats["wrr"])-1)
				index = max(index, 0)
				lats[i] = _lats["wrr"][index]*np.random.normal(1,0.1)
				# thrg[i] += _thrg["wrr"][index]*np.random.normal(1,0.1)
				util[i] = min(1,lats[i]/_lats["wrr"][-2])
			else:
				util[i] = util[i-1]* real_prop/(prop)

		lo = list(map(add, lo, load))
		la = list(map(add, lats, la))
		th = list(map(add, thrg, th))
		ut = list(map(add, util, ut))

	return np.divide(lo,100), np.divide(la,100), np.divide(th,100), np.divide(ut,100)

def avg(x):
	if len(x)!=0:
		return sum(x)/len(x)
	else:
		return 0

def check(u, u_prim, w, accelerators): 
	if avg(u)<avg(u_prim) and avg(u)< 0.85:
		print("check")
		return 0
	if w == 0:
		u = u[0:-1:accelerators+1]
		if avg(u) >= 0.8:
			return 0
		else:
			return 1
	else:
		if max(u)>=1:
			return 0
		else: 
			return 1

def find_w(u, u_prim, w, accelerators):
	if avg(u)<avg(u_prim) and avg(u)< 0.85:
		return 0
	return w+1

weight = 0
def smart(rate, server, accelerators, w):
	global weight
	u_prim = []
	lo, la, t ,u = wrr(rate, server, accelerators, w)
	flag = check(u, u_prim, w, accelerators)
	while (not flag):
		# if weight == 0:
		# 	w = find_w(u, u_prim, w, accelerators)
		# elif np.random.rand() > 0.8:
		# 	w = find_w(u, u_prim, w, accelerators)
		# else:
		# 	print("previous")
		# 	w = weight
		w = find_w(u, u_prim, w, accelerators)
		lo, la, t ,u = wrr(rate, server, accelerators, w)
		flag = check(u, u_prim, w, accelerators)
	weight = w
	return la[0:-1:accelerators+1],u, w


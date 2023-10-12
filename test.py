from simulation import *
from operator import add
import numpy as np
import csv

def avg(x):
	if len(x)!=0:
		return sum(x)/len(x)
	else:
		return 0

def check(u, u_prim, w, accelerators): 
	if avg(u)<avg(u_prim) and avg(u)< 0.85:
		# print("check")
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
		print("fine")
		return 0
	return w+1

server = 128
accelerators = 2
w = 0


u_prim = []
best_lat = []
# for i in range(1000):
# 	w=0
# 	print(smart(100*16, server, accelerators, w))
# for rate in range(20, 42, 2):
# 	w=0
# 	la = smart(rate, server, accelerators, w)
# 	best_lat.append(avg(la))

# for rate in range(40, 20, -2):
# 	w=0
# 	la = smart(rate, server, accelerators, w)
# 	best_lat.append( avg(la))
# f=open('data.csv','ab')
data = []
f=open('data2.csv','ab')

for i in range(5):
	for rate in range(128*8,128*20,16):
		w=0
		print(rate, i)
		l,u,w = smart(rate, server, accelerators, w)
		x = np.append(u,w).reshape(1,(accelerators+1)*128+1)
		np.savetxt(f, x, fmt='%10.5f', delimiter=",")


print(best_lat)

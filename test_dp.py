from simulation import *
import pickle
import numpy as np
import random

with open('q_table2.pkl', 'rb') as file:
	q_table = pickle.load(file)


def policy(state, q_table):
	row = q_table[state]
	if random.random() > 0.1:
		return row.index(max(row))
	else:
		return random.randint(0, 2)

def reward(u, accelerators, lats, w):
	if np.average(u_accelerators(u, accelerators)) > 1:
		return -10
	elif w == 0 and np.percentile(lats,99) < 1000:
		return 10
	elif np.average(ut[::accelerators+1]) > 0.60 and np.average(u_accelerators(u, accelerators)) < 1 and np.percentile(lats,99) <1300:
		return 10
	return -1
def u_accelerators (u, accelerators):
	u_a = []
	for i in range(len(u)):
		if i%accelerators!=0:
			u_a.append(u[i])
	return u_a

server = 200
accelerators = 2

for i in range(6,23):
	ls = []
	ws = []
	for j in range(100):
		rate = server * i
		# rate = server * 16
		weight = 7
		w = 0
		while True:
			load, lat, thr, ut = wrr(rate, server, accelerators, w)
			index = int(np.average(ut[::accelerators+1])*20)
			a = policy(index, q_table)
			if a == 0: weight -= 1
			if a == 2: weight += 1
			weight = min(7, weight)
			weight = max(0, weight)
			w = weight
			if w == 7: w = 0
			load_2, lat_2, thr_2, ut_2 = wrr(rate, server, accelerators, w)
			r = reward(ut_2, accelerators, lat_2, w)
			index_2 = int(np.average(ut_2[::accelerators+1])*20)
			try:
				# print("here")
				q_table[index][a] = q_table[index][a] + 0.1*(r + 0.9*q_table[index_2][a]- q_table[index_2][a])
			except:
				# print("not here")
				q_table[int(np.average(ut)*20)][a] = -100
			if r == 10 or r == -10:
				break
		# print(np.percentile(lat_2,99))
		ls.append(np.percentile(lat_2,99))
		ws.append(w)
	print(f'rate:{rate}, w: {sum(ws)/len(ws)}, P99: {sum(ls)/len(ls)}')



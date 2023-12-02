from simulation import *
import pickle
import numpy as np
import random

with open('64-2.pkl', 'rb') as file:
	rate_128 = pickle.load(file)
	thrg_128 = pickle.load(file)
	lats_128 = pickle.load(file)



def u_accelerators (u, accelerators):
	u_a = []
	for i in range(len(u)):
		if i%accelerators!=0:
			u_a.append(u[i])
	return u_a

def reward(u, accelerators, lats, w):
	if np.average(u_accelerators(u, accelerators)) > 1:
		return -10
	elif w == 0 and np.percentile(lats,99) < 1000:
		return 10
	elif np.average(ut[::accelerators+1]) > 0.60 and np.average(u_accelerators(u, accelerators)) < 1 and np.percentile(lats,99) <1300:
		return 10
	return -1


def find_index(u, w):
	index = int(np.average(ut[::accelerators+1])*20)
	index = min(20, index)
	if w !=0:
		index += 10
	return index


server = 10
accelerators = 2

def policy(state, q_table):
	# print(state)
	row = q_table[state]
	if random.random() > 0.1:
		return row.index(max(row))
	else:
		return random.randint(0, 2)


q_table = [[0,0,0] for i in range(40)]

server = 128
accelerators = 2

weight = 7
w = 0
for i in range(10000):
	rate = server * random.randint(2, 24)
	# rate = server * 10
	# rate = server //50
	# weight = 7
	# w = 0
	# load, lat, thr, ut = wrr(rate, server, accelerators, w)
	# r = reward(ut, accelerators, lat, w)
	# print(f'{i}, rate:{rate}, reward:{r}, P99: {np.percentile(lat,99)}, U: {np.average(ut[::accelerators+1])}')
	while True:
		load, lat, thr, ut = wrr(rate, server, accelerators, w)
		# index = int(np.average(ut[::accelerators+1])*20)
		index = find_index(ut, w)
		a = policy(index, q_table)
		if a == 0: weight -= 1
		if a == 2: weight += 1
		weight = min(7, weight)
		weight = max(0, weight)
		w = weight
		if w == 7: w = 0

		load_2, lat_2, thr_2, ut_2 = wrr(rate, server, accelerators, w)
		r = reward(ut_2, accelerators, lat_2, w)
		index_2 = find_index(ut_2, w)
		try:
			# print("here")
			para = 0.5*(r + 0.9*q_table[index_2][a]- q_table[index_2][a])
			q_table[index][a] = q_table[index][a] + para
			if para>0:
				print(para)
		except:
			# print("not here")
			q_table[int(np.average(ut)*20)][a] = -100
		# print(f'w: {w}, rate:{rate}, reward:{r}, P99: {np.percentile(lat_2,99)}, U: {np.average(ut_2[::accelerators+1])}')
		# ut = ut_2
		# print("****************")
		if r == 10 or r == -10:
			break
	print(f'i:{i}, rate:{rate}, w: {w}, P99: {np.percentile(lat_2,99)}')


for i in range(40):
	print(i*5, q_table[i])

with open('dp_59.pkl', 'wb') as file:
	pickle.dump(q_table, file)







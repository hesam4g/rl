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


# for i in range(5,21):
# 	rate = server*i
# 	load, lat, thr, ut = wrr(rate, server, accelerators, 0)
# 	print(rate)
# 	print(0, np.average(ut[::accelerators+1]), np.average(ut), np.percentile(lat,99))

# 	load, lat, thr, ut = wrr(rate, server, accelerators, 6)
# 	print(6, np.average(ut[::accelerators+1]), np.average(ut), np.percentile(lat,99))

# 	print("****************")

# for i in range(10):

# 	load, lat, thr, ut = wrr(1300, server, accelerators, i)
# 	print(rate)
# 	print(i, np.average(ut[::accelerators+1]), np.average(u_accelerators(ut, accelerators)), np.percentile(lat,99))

# 0 increase w
# 1 nothing to w
# 2 decrease w
server = 10
accelerators = 2

def policy(state, q_table):
	row = q_table[state]
	if random.random() > 0.1:
		return row.index(max(row))
	else:
		return random.randint(0, 2)


q_table = [[0,0,0] for i in range(20)]

server = 100
accelerators = 2
# rate = 8*server
# load, lat, thr, ut = wrr(rate, server, accelerators, 0)
# print(0, np.average(ut[::accelerators+1]), np.average(ut), np.percentile(lat,99))
# load, lat, thr, ut = wrr(rate, server, accelerators, 0)
# print(6, np.average(ut[::accelerators+1]), np.average(ut), np.percentile(lat,99))


for i in range(100):
	rate = server * random.randint(2, 24)
	# rate = server * 10
	# rate = server //50
	weight = 7
	w = 0
	# load, lat, thr, ut = wrr(rate, server, accelerators, w)
	# r = reward(ut, accelerators, lat, w)
	# print(f'{i}, rate:{rate}, reward:{r}, P99: {np.percentile(lat,99)}, U: {np.average(ut[::accelerators+1])}')
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
			para = 0.1*(r + 0.9*q_table[index_2][a]- q_table[index_2][a])
			q_table[index][a] = q_table[index][a] + 0.1*(r + 0.9*q_table[index_2][a]- q_table[index_2][a])
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


for i in range(20):
	print(i*5, q_table[i])

with open('q_table_200_1000.pkl', 'wb') as file:
	pickle.dump(q_table, file)







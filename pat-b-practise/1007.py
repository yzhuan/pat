import math

num = int(raw_input())
max_num = 100000
prime_tbl = [0] * max_num
prime = []
for i in range(2, max_num):
	if prime_tbl[i] == 0:
		prime.append(i)
		prime_tbl[i] = 1
		for j in range(2*i, max_num, i):
			prime_tbl[j] = 1
cnt = [0] * max_num
for i in range(1, len(prime)):
	for j in range(prime[i-1], prime[i]):
		cnt[j] = cnt[prime[i-1]]
	if prime[i] - prime[i-1] == 2:
		cnt[prime[i]] = cnt[prime[i-1]] + 1
	else:
		cnt[prime[i]] = cnt[prime[i-1]]
for i in range(prime[-1], max_num):
	cnt[i] = cnt[prime[-1]]
print cnt[num]

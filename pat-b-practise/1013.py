max_num = 110000
prime_tbl = [0]*max_num
prime = []
for i in range(2,max_num):
	if prime_tbl[i] == 1:
		continue
	prime.append(i)
	for j in range(i,max_num,i):
		prime_tbl[j] = 1
#print len(prime)
num = [int(item) for item in raw_input().split()]
rlt = ""
cnt = 0
for i in range(num[0]-1,num[1]):
	if cnt != 0:
		rlt += " "
	cnt += 1
	rlt += str(prime[i])
	if cnt == 10:
		print rlt
		cnt = 0
		rlt = ""
if len(rlt) > 0:
	print rlt	

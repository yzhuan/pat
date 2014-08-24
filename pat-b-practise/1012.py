num = [int(item) for item in raw_input().split()]
num = num[1::]
A = [None]*5
for i in range(5):
	A[i] = list()
for item in num:
	A[item % 5].append(item)
rlt = ""
A[0] = filter(lambda x: x % 2 == 0 ,A[0])
if len(A[0]) == 0:
	rlt += "N "
else:
	rlt += "%d " % (sum(A[0]))
if len(A[1]) == 0:
	rlt += "N "
else:
	cnt = 0
	for i in range(len(A[1])):
		cnt += (-1)**i * A[1][i]
	rlt += "%d " % (cnt)
if len(A[2]) == 0:
	rlt += "N "
else:
	rlt += "%d " % (len(A[2]))
if len(A[3]) == 0:
	rlt += "N "
else:
	rlt += "%.1f " % (sum(A[3])/float(len(A[3])))
if len(A[4]) == 0:
	rlt += "N"
else:
	rlt += "%d" % (max(A[4]))
print rlt

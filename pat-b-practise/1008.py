n,m = raw_input().split()
n = int(n)
m = int(m) % n
l = raw_input().split()
l = l[-m::] + l[:-m]
rlt = ""
for i in range(len(l)):
	if i > 0:
		rlt += " "
	rlt += l[i]
print rlt

T = int(raw_input())
for i in range(T):
	num = [int(item) for item in raw_input().split()]
	rlt = "Case #%d: " % (i+1)
	if num[0] + num[1] > num[2]:
		rlt += "true"
	else:
		rlt += "false"
	print rlt

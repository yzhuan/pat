cnt = int(raw_input())
num = [int(item) for item in raw_input().split()]
hist = list(num)
for item in num:
	while item != 1:
		if item & 0x1 == 0:
			item = item / 2
			hist.append(item)
		else:
			item = (item * 3 + 1) / 2
			hist.append(item)
dic = {item:hist.count(item) for item in hist}
rlt = []
for item in dic:
	if dic[item] == 1:
		rlt.append(item)
rlt = sorted(rlt, reverse = True)
rlt_str = ""
for pos in range(len(rlt)):
	if pos != 0:
		rlt_str += " "
	rlt_str += str(rlt[pos])
print rlt_str
	

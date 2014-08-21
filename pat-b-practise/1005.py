cnt = int(raw_input())
num = [int(item) for item in raw_input().split()]
root = list(num)
child = dict()

for item in num:
	while item != 1:
		if item & 0x1 == 0:
			item = item / 2
			child[item] = True
		else:
			item = (item * 3 + 1) / 2
			child[item] = True
rlt = []
for item in root:
	if not child.has_key(item):
		rlt.append(item)
rlt = sorted(rlt, reverse = True)
rlt_str = ""
for pos in range(len(rlt)):
	if pos != 0:
		rlt_str += " "
	rlt_str += str(rlt[pos])
print rlt_str
	

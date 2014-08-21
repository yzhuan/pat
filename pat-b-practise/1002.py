chn_list = ["ling","yi","er","san","si","wu","liu","qi","ba","jiu"]

def Solution(line):
	total = sum([int(item) for item in line])
	rlt = []
	if total == 0:
		rlt.append(chn_list[0])
	while total > 0:
		rlt.append(chn_list[total%10])
		total = int(total/10)
	rlt = rlt[::-1]
	rlt_str = ""
	for i in range(len(rlt)):
		if i > 0:
			 rlt_str += " "
		rlt_str += rlt[i]
	return rlt_str
line = raw_input()
print Solution(line)

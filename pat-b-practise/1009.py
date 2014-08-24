words = raw_input().split()
words = words[::-1]
rlt = ""
for i in range(len(words)):
	if i > 0:
		rlt += " "
	rlt += words[i]
print rlt

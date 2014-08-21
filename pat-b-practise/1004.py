from operator import itemgetter, attrgetter
cnt = int(raw_input())
data = []
while cnt > 0:
	cnt -= 1
	attr = raw_input().split()
	attr[2] = int(attr[2])
	line = tuple(attr)
	data.append(line)
#print data
data = sorted(data, key = itemgetter(2), reverse = True)
#print data
print "%s %s" % (data[0][0], data[0][1])
print "%s %s" % (data[-1][0], data[-1][1])

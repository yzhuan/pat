class Record:
	def __init__(self, id, de, cai):
		self.id = id
		self.de = de
		self.cai = cai
		self.total = de + cai
	def __str__(self):
		return "%d %d %d" % (self.id, self.de, self.cai)
	def __cmp__
arg = [int(item) for item in raw_input().split()]
N = arg[0]
L = arg[1]
H = arg[2]
tbl = [None] * 4
for i in range(4):
	tbl[i] = list()
for i in range(N):
	line = [int(item) for item in raw_input().split()]
	r = Record(line[0], line[1], line[2])
	if r.de < L or r.cai < L:
		continue
	if r.de >= H and r.cai >= H:
		tbl[0].append(r)
	elif r.de >= H and r.cai < H:
		tbl[1].append(r)
	elif r.de < H and r.cai < H and r.de >= r.cai:
		tbl[2].append(r)
	else:
		tbl[3].append(r)
def Record_cmp(rec_a, rec_b):
	if rec_a.total != rec_b.total:
		return rec_a.total > rec_b.total
	if rec_a.de != rec_b.de:
		return rec_a.de < rec_b.de
	return rec_a.id < rec_b.id
#for i in range(4):
#	tbl[i].sort(Record_cmp)
rlt = tbl[0] + tbl[1] + tbl[2] + tbl[3]
for r in rlt:
	print r
print len(tbl[0]) + len(tbl[1]) + len(tbl[2]) + len(tbl[3])


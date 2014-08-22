num = int(raw_input())
a = int(num / 100)
b = int(num % 100 / 10)
c = int(num % 10)
rlt = ""
for i in range(a):
	rlt += "B"
for i in range(b):
	rlt += "S"
for i in range(c):
	rlt += str(i + 1)
print rlt

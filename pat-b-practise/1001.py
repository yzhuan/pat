
def Solution(n):
	cnt = 0
	while True:
		if n == 1:
			return cnt
		if n&0x1 == 1:
			n = 3*n + 1
		n = n >> 1
		cnt += 1
line = raw_input()
print Solution(int(line))
			

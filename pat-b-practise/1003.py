def Solution(line):
	 rlt_str = ["NO", "YES"]
	 str_len = len(line)
	 cnt_a = 0
	 cnt_b = 0
	 cnt_c = 0
	 pos = 0
	 while pos < str_len and line[pos] == 'A':
		pos += 1
		cnt_a += 1
	 if pos < str_len and line[pos] != 'P':
		return rlt_str[0]
	 else:
		pos += 1
	 while pos < str_len and line[pos] == 'A':
		pos += 1
		cnt_b += 1
	 if pos < str_len and line[pos] != 'T':
		return rlt_str[0]
	 else:
		pos += 1
	 while pos < str_len and line[pos] == 'A':
		pos += 1
		cnt_c += 1
	 if pos != str_len:
		return rlt_str[0]
	 if cnt_a != 0 and (cnt_c - cnt_a) / cnt_a == cnt_b - 1:
		return rlt_str[1]
	 if cnt_a == 0 and cnt_c == 0 and cnt_b > 0:
		return rlt_str[1]
	 if cnt_a == cnt_c and cnt_b == 1:
		return rlt_str[1]
	 return rlt_str[0]
cnt = int(raw_input())
while cnt > 0:
	cnt = cnt - 1
	line = raw_input()
	print Solution(line)


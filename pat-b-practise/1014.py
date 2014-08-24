week = {"A":"MON","B":"TUE","C":"WED","D":"THU","E":"FRI","F":"SAT","G":"SUN"}
time = "0123456789ABCDEFGHIJKLMN"
line = [None] * 4
for i in range(4):
	line[i] = raw_input()
flag = 0
rlt = ""
cnt = min(len(line[0]),len(line[1]))
for i in range(cnt):
	if flag == 0:
		if line[0][i] >= 'A' and line[0][i] <= 'G' and line[0][i] == line[1][i]:
			rlt += week[line[0][i]]
			flag = 1
	else:
		if ((line[0][i] >= 'A' and line[0][i] <= 'N') or (line[0][i] >= '0' and line[0][i] <= '9')) and line[0][i] == line[1][i]:
			rlt += " %02d:" % (time.index(line[0][i]))
			break
cnt = min(len(line[2]),len(line[3]))
for i in range(cnt):
	if ((line[2][i] >= 'A' and line[2][i] <= 'Z') or (line[2][i] >= 'a' and line[2][i] <= 'z')) and line[2][i] == line[3][i]:
		rlt += "%02d" % (i)
		break
print rlt	
			


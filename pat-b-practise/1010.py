# TO BE CORRECTED
coff = [int(item) for item in raw_input().split()]
flag = 0
rlt = ""
for i in range(0,len(coff),2):
	if coff[i+1] * coff[i] > 0:
		if flag == 0:
	        flag = 1
	    else:
	        rlt += " "
		rlt += str(coff[i]*coff[i+1])
		rlt += " "
		rlt += str(coff[i+1]-1)
if flag == 0:
	rlt += "0 0"
print rlt

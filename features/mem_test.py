#!/usr/local/lib
# -*- coding: UTF-8 -*-

import os

f = open("./ShowProcess.py",'r')
lines_f = f.readlines()
# print lines_f
f.close()
for i in range(0, len(lines_f)):
	if "def" in lines_f[i]:
		if "#" not in lines_f[i]:
			j = 0
			k = 0
			flag = 0
			while True:
				if lines_f[i][j] == "d":
					flag = 1
					break
				if lines_f[i][k] == "d":
					break
				if ord(lines_f[i][j]) == 32:
					j += 1
				if ord(lines_f[i][j]) == 9:
					k += 1
			a = ""
			if j != 0:
				for t in range(0,j):
					a += " "
			if k != 0:
				for t in range(0,k):
					a += "\t"	
			# if flag == 1:
			lines_f[i-1] = lines_f[i-1] + a +  "@profile\n"

			# lines_f[i-1]
con = ""
f = open("./ShowProcess.py",'w')
for i in range(0, len(lines_f)):
	con += lines_f[i]
f.write(con)
f.close()

	# name = label.split(".")[0] + ".txt"
	# if "training" in path:
	# 	f = open(os.path.join("trainingfeature",name), 'a')
	# if "testing" in path:
	# 	f = open(os.path.join("testingfeature",name), 'a')
	# for i in range(0,len(features)):
	# 	f.write(str(features[i]))
	# 	f.write(",")
	# # f.write(data)
	# # f.write('\n')
	# f.close()


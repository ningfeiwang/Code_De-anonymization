#!/usr/local/lib
# -*- coding: UTF-8 -*-

import os

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list


for path in ["./testing", "./training"]:
	if "training" in path:
		print "training"
	if "testing" in path:
		print "testing"
	name_list = get_name(path)
	for each in name_list:
		print each
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		# print lines_f
		f.close()
		for i in range(0, len(lines_f)):
			if "def " in lines_f[i]:
				if "#" not in lines_f[i]:
					if "'" not in lines_f[i]:
						if '"' not in lines_f[i]:
							j = 0
							k = 0
							flag = 0
							tmp = 0
							while True:
								tmp += 1
								if tmp == 1000:
									break
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
				if tmp == 1000:
					continue
				con = ""
				f = open(os.path.join(path,each),'w')
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


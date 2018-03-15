#!/usr/local/bin/python
# coding:utf-8

import os
from os.path import join, getsize

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

# def get_FileSize(filePath):
def getdirsize(dir):  
   size = 0L  
   for root, dirs, files in os.walk(dir):  
      size += sum([getsize(join(root, name)) for name in files])  
   return size/float(1024)  

def get_file(filename):
	print filename
	code_list = get_name(filename)
	# i = "du -sh " + filename
	i = getdirsize(filename)
	# print i
	if i > 80.0:
	# if os.system(i) >
		if len(code_list) > 10:
			ins = "cp" + " -r " + filename + " " + os.path.join("/Users/wangningfei/Documents/Code_De-anonymization-ningfei/dataset/codejamfolder2", "data")
			print ins
			os.system(ins)
			print 1
			return 1
			# cnt += 1
	else:
		return 0

if __name__ == '__main__':
	os.system("mkdir data")
	global path
	# global cnt
	cnt = 0
	# cnt = 0
	path = "/Users/wangningfei/Documents/Code_De-anonymization-ningfei/dataset/codejamfolder2/py"
	name_list = get_name(path)
	# print name_list[0]
	count = 0
	for each in name_list:
		if each =='.DS_Store':
			continue
		k = get_file(os.path.join(path,each))
		count += 1
		if k == 1:
			cnt += 1
	print "total code numver: " + str(count)
	print "after cleaning: " + str(cnt)

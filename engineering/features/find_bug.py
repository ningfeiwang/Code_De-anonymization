#!/usr/local/bin/python
# coding:utf-8

import os

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def readfile(filename):
	with open(filename) as file:
		data = file.readlines()
	return data



if __name__ == '__main__':
	nums = 0
	global path
	# os.system("mkdir traininglog")
	# os.system("mkdir testinglog")
	for i in range(0,2):
		if i == 0:
			path = "./testingfeature"
		else:
			path = "./trainingfeature"
		name_list = get_name(path)
		for each in name_list:
			if each == ".DS_Store":
				continue
			data = readfile(os.path.join(path,each)
			if data[0].split(',') != nums:
				print each

	# k = 500
	# file = 'a'
	# # print name_list
	# for each in name_list:
	# 	if (each == '.DS_Store'):
	# 		continue
	# 	filename = get_name(os.path.join(path,each))
	# 	if (k > len(filename)):
	# 		k = len(filename)
	# 		file = each
	# print k 
	# print file
	# key_word = readfile("python_keyword.txt")

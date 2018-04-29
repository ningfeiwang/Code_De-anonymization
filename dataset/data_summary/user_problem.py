#!/usr/local/bin/python
# coding:utf-8

import os
from os.path import join, getsize

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def readfile(filename):
	with open(filename) as file:
		data = file.read()
	return data

if __name__ == '__main__':
	global path
	path = "./training"
	name_list = get_name(path)
	problem = {}
	user = {}
	i = 1		
	for each in name_list:
		if (each == '.DS_Store'):
			continue
		
		# filename = get_name(os.path.join(path,each))
		k_p = os.path.join(path,each)
		# k = 0

		# for file in filename:
		if (each == '.DS_Store'):
			continue
		# print file
		pro = each.split("_")[0]
		use = each.split("_")[1].split(".")[0]
		problem[pro] = i
		user[use] = i
		i += 1
	print len(problem.keys())
	print len(user.keys())

			# print pro
			# print use
			# break
		# break
			# print len(n)

		# data = readfile(os.path.join(path, each))

			# l = len(data)
	# print l



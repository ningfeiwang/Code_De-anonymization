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

def writefile(filename, data):
	log = open(filename, 'a')
	log.write(data)
	log.write('\n')
	log.close()

if __name__ == '__main__':
	global path
	path = "/Users/ningfeiwang/Documents/spring2018/cse498_info_privacy/project/Code_De-anonymization/dataset/data/data_80k_74"
	name_list = get_name(path)
	for each in name_list:
		if (each == '.DS_Store'):
			continue
		
		filename = get_name(os.path.join(path,each))
		k_p = os.path.join(path,each)
		k = 0
		for file in filename:
			if (file == '.DS_Store'):
				continue
			if k <= 2:
				name = "testing/" + each + ".py"
				data = readfile(os.path.join(k_p,file))
				writefile(name, data)
				k += 1
			else:
				name = "training/" + each + ".py"
				data = readfile(os.path.join(k_p,file))
				writefile(name, data)
			# print len(n)

		# data = readfile(os.path.join(path, each))

			# l = len(data)
	# print l



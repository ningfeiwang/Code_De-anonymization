#!/usr/local/bin/python
# coding:utf-8

import os

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def readfile(filename):
	with open(filename) as file:
	data = file.read()
	return data

if __name__ == '__main__':
	global path
	path = '/Users/ningfeiwang/Documents/spring2018/cse498_info_privacy/project/Code_De-anonymization/dataset/data/data_80k_74'
	name_list = get_name(path)
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
	key_word = readfile("python_keyword.txt")

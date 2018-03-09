#!/usr/local/bin/python
# coding:utf-8

import os

def get_name(filename):
	name_list = os.listdir(filepath)
	return name_list

def get_file(filename):
	code_list = get_name(filename)
	if len(code_list) > 2:
		ins = "mv" + filename + " " + os.path.join(path, "data")
		os.system(ins)
	else:
		return 0

if __name__ == '__main__':
	mkdir data
	global path
	path = ****
	name_list = get_name(path)
	for each in name_list:
		get_file(os.path.join(path,each))

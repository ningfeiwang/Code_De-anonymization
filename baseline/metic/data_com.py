#!/usr/local/bin/python
# coding:utf-8

import os

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

if __name__ == '__main__':
	os.system("rm -rf training_com")
	os.system("rm -rf testing_com")
	# os.system("rm -rf traininglog")
	# os.system("rm -rf testinglog")
	global path
	os.system("mkdir training_com")
	os.system("mkdir testing_com")
	# os.system("mkdir traininglog")
	# os.system("mkdir testinglog")
	for i in range(0,2):
		if i == 0:
			path = "./testing"
		else:
			path = "./training"
		name_list = get_name(path)
		
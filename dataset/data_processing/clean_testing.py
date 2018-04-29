#!/usr/local/bin/python
# coding:utf-8

import os
import re
# import math

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

if __name__ == '__main__':
	# name_list = get_name(os.path.join("./", "training_1"))
	test_name = get_name("./testing")
	train_name = get_name("./training")

	usertest = []
	usertrain = []
	for each in train_name:
		if each == ".DS_Store":
			continue
		usertrain.append(each.split("_")[1])

	for each in test_name:
		if each == ".DS_Store":
			continue
		if each.split("_")[1] not in usertrain:
			cmd = 'rm ./testing/'



	

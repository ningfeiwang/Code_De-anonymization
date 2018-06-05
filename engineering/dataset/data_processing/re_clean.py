#!/usr/local/bin/python
# coding:utf-8

import os
import re
# import math

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

if __name__ == '__main__':
	name_list = get_name(os.path.join("./", "training_1"))
	user = []
	for each in name_list:
		if each == ".DS_Store":
			continue
		pos = each.rfind('_')
		name = each[:pos]
		# if name not in user:
		user.append(name)
	for kkk in user:
		cnt = user.count(kkk)
		if cnt > 2:
			continue
		else:
			cmd = "rm ./training_1/" + kkk + "*.py"
			os.system(cmd) 
	

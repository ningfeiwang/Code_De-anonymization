#!/usr/local/bin/python
# coding:utf-8

import os
import re
# import math

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

if __name__ == '__main__':
	# os.system("sudo rm -r new_training")
	# os.system("sudo rm -r new_testing")
	name = get_name("./")
	os.system("mkdir training_1")
	os.system("mkdir testing_1")
	for k in ["new_training", "new_testing"]:
		name_list = get_name(os.path.join("./", k))
		for each in name_list:
			if each == ".DS_Store":
				continue
			path = "./" + k + "/" + each
			f = open(path,'r')
			lines_f = f.readlines()
			# print lines_f
			f.close()
			flag = 0
			for line in lines_f:
				if "error" in line:
					flag = 1
			if flag == 1:
				continue
			else:
				if "train" in k:
					cmd = "cp ./training/" + each.split(".log")[0] + " ./training_1/"
				else:
					cmd = "cp ./testing/" + each.split(".log")[0] + " ./testing_1/"
				os.system(cmd)

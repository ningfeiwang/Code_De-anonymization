#!/usr/local/bin/python
# coding:utf-8

import os
import re
# import math

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def readfile(filename):
	with open(filename) as file:
		data = file.read()
	return data

if __name__ == '__main__':
	# os.system("sudo rm -r new_training")
	# os.system("sudo rm -r new_testing")
	name_list = get_name("./data_80k_74")
	# os.system("mkdir ../training_1")
	os.system("mkdir ./data")
	for each in name_list:
		if each == ".DS_Store":
			continue
		name_code = get_name("./data_80k_74/" + each)
		for name in name_code:
			cmd = "cp ./data_80k_74/" + each + "/" + name + " ./data"
			print cmd
			os.system(cmd)
		# f = open("./new_data/"+each,'r')
		# try:
		# 	lines_f = f.readlines()
		# except:
		# 	continue
		# # print lines_f
		# f.close()
		# flag = 0
		# for line in lines_f:
		# 		if "error" in line:
		# 			flag = 1
		# 		if "Error" in line:
		# 			flag = 1
		# if flag == 1:
		# 		continue
		# else:
		# 	pos = each.split(".log")[0].find('_')
		# 	name = each.split(".log")[0][pos+1:]
		# 	cmd = "cp ./data_80k_74/" + name.split(".py")[0] + "_0/" + each.split(".log")[0] + " ./data/"
		# 	os.system(cmd)
	# for k in ["new_training", "new_testing"]:


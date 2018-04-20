#!/usr/local/bin/python
# coding:utf-8

import os
import re
import math

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def readfile(filename):
	with open(filename) as file:
		data = file.read()
	return data

if __name__ == '__main__':
	os.system("sudo rm -r new_training")
	os.system("sudo rm -r new_testing")
	name = get_name("./")
	os.system("mkdir new_training")
	os.system("mkdir new_testing")
	for k in name:
		if k == ".DS_Store":
			continue
		if "cmd" in k:
			continue
		name_list = get_name(os.path.join("./",k))
		for each in name_list:
			if each == ".DS_Store":
				continue
			if "train" in k:
# nohup python2 mil_test.py> log.txt 2>&1 &
				cmd = "nohup python2 ./" + k + "/" + each + " > ./new_training/" + each + ".log 2>&1 &"
				os.system(cmd)
			else:
# nohup python2 mil_test.py> log.txt 2>&1 &
				cmd = "nohup python2 ./" + k + "/" + each + " > ./new_testing/" + each + ".log 2>&1 &"
				os.system(cmd)


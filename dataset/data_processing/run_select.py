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
	name_list = get_name("./sample_input")
	input_pid = []
	os.system("sudo rm -r new_data")
	os.system("mkdir new_data")
	for i in range(0, len(name_list)):
		if ".DS_Store" in name_list[i]:
			continue
		input_pid.append(name_list[i].split(".txt")[0])

	name_list = get_name("./data_80k_74")

	for each in name_list:
		if (each == '.DS_Store'):
			continue
		
		filename = get_name(os.path.join("./data_80k_74",each))
		# k_p = os.path.join(path,each)
		# k = 0
		for file in filename:
			if (file == '.DS_Store'):
				continue
			name = file.split("_")[0]
			name = name[1:]
			if name in input_pid:
				cmd = "nohup python2 ./data_80k_74/" + each + "/" + file +" < ./sample_input/" + name + ".txt" + " > ./new_data/" + file + ".log 2>&1 &"
				os.system(cmd)
			else:
				cmd = "nohup python2 ./data_80k_74/" + each + "/" + file + " > ./new_data/" + file + ".log 2>&1 &"
				os.system(cmd)















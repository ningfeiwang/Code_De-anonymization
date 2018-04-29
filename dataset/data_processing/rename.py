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

	name = get_name("./data")
	username = []
	for k in name:
		if k == ".DS_Store":
			continue
		if "cmd" in k:
			continue
		i = 0
		while(1):
			pos = k.split(".py")[0].find('_')
			tmp = k.split(".py")[0][pos+1:]
			name = tmp + '_' + str(i)
			if name not in username:
				username.append(name)
				cmd = 'mv ./data/' + k + ' ./data/' + k.split(".py")[0][:pos+1] + name + '.py'
				os.system(cmd)
				break
			else:
				i += 1
#!/usr/local/bin/python
# coding:utf-8

import os
from os.path import join, getsize

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def readfile(filename):
	with open(filename) as file:
		data = file.read()
	return data

def writefile(filename, data):
	log = open(filename, 'a')
	log.write(data)
	log.write('\n')
	log.close()

if __name__ == '__main__':
	global path
	path = "./data"
	name_list = get_name(path)
	os.system("mkdir training")
	os.system("mkdir testing")
	for each in name_list:
		if (each == '.DS_Store'):
			continue
		
		pos = each.split('.py')[0].rfind('_')
		num = each.split('.py')[0][pos+1:]
		if int(num) <= 4:
			cmd = "cp ./data/" + each +" ./testing/"
		else:
			cmd = "cp ./data/" + each +" ./training/"
		os.system(cmd)

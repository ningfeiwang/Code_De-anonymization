#!/usr/local/bin/python
# coding:utf-8

import os
import re
import math

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def writefile(data):
	log = open("./trainingname.txt", 'a')
	log.write(data)
	log.write('\n')
	log.close()

name_list = get_name("./training")
for name in name_list:
	if name == ".DS_Store":
		continue
	writefile(name)
#!/usr/local/bin/python
# coding:utf-8

import os
from os.path import join, getsize
import re
import math
import time
from ShowProcess import ShowProcess
# import ast
# import ast_visit

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def readfile(filename):
	with open(filename) as file:
		data = file.read()
	return data

def get_length(filename):
	f = open(os.path.join(path,filename),'r')
	lines_f = f.readlines()
	# print lines_f
	f.close()
	return len(lines_f)

def writefeatures(label,features):
	name = label.split(".txt")[0] + ".txt"
	if "training" in path:
		f = open(os.path.join("trainingfeature",name), 'a')
	if "testing" in path:
		f = open(os.path.join("testingfeature",name), 'a')
	for i in range(0,len(features)):
		f.write(str(features[i]))
		f.write(",")
	# f.write(data)
	# f.write('\n')
	f.close()

def nums_lenline(name_list):
	# lenline = {}
	if "training" in path:
		print "training lines length"
	if "testing" in path:
		print "testing lines length"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		# lenline[each] = [float(len(lines_f))]
		writefeatures(each, [float(len(lines_f))])


def comment_len(name_list):
	comment = {}
	if "training" in path:
		print "training comment length"
	if "testing" in path:
		print "testing comment length"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		com = 0
		for i in range(0, len(lines_f)):
			if "#" in lines_f[i]:
				com += 1
		if com == 0:
			com = 1
		comment[each] = [float(math.log(com))]
		# print comment
		writefeatures(each, comment[each])

def get_par(name_list):
	if "training" in path:
		print "training par"
	if "testing" in path:
		print "testing par"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		try:
			root = ast.parse(open(os.path.join(path,each)).read())
		except:
			writefeatures(each, [float(0),float(0)]) #big first, big num and _ nums, li nums
			continue

		names = sorted({node.id for node in ast.walk(root) if isinstance(node, ast.Name)})

		if len(names) == 0:
			writefeatures(each, [float(0),float(0)]) #big first, big num and _ nums, li nums
			continue
		tmp = 0
		# sum_l = 0
		for i in range(0, len(names)):
			tmp += len(names[i])

		writefeatures(each, [float(float(tmp)/float(len(names))), float(len(names))])

def loop(name_list):
	comment = {}
	if "training" in path:
		print "training comment length"
	if "testing" in path:
		print "testing comment length"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		a = 0
		b = 0
		for i in range(0, len(lines_f)):
			if "for" in lines_f[i]:
				a += 1
				b += 1
			if 'while' in lines_f[i]:
				b += 1
		if b == 0:
			b = 1
		comment[each] = [float(float(a)/float(b))]
		# print comment
		writefeatures(each, comment[each])

def getdirsize(dir):  
   size = 0L  
   for root, dirs, files in os.walk(dir):  
      size += sum([getsize(join(root, name)) for name in files])  
   return size 

def get_size():
	comment = {}
	if "training" in path:
		print "training comment length"
		p = './trainingzip'
	if "testing" in path:
		print "testing comment length"
		p = './testingzip'
	name_list = get_name(p)
	process_bar = ShowProcess(len(name_list)-1)

	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		size = getdirsize(os.path.join(p,each))
		
		if size == 0L:
			size = 1
		comment[each] = [float(math.log(float(size)))]
		# print comment
		writefeatures(each.split('.zip')[0], comment[each])

if __name__ == '__main__':
	os.system("rm -rf trainingfeature")
	os.system("rm -rf testingfeature")
	# os.system("rm -rf traininglog")
	# os.system("rm -rf testinglog")
	global path
	os.system("mkdir trainingfeature")
	os.system("mkdir testingfeature")
	# os.system("mkdir traininglog")
	# os.system("mkdir testinglog")
	for i in range(0,2):
		if i == 0:
			path = "./testing"
		else:
			path = "./training"
		name_list = get_name(path)
		nums_lenline(name_list)
		comment_len(name_list)
		get_par(name_list)
		loop(name_list)
		get_size()
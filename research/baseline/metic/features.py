#!/usr/local/bin/python
# coding:utf-8

import os
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

def line_size(name_list):
	if "training" in path:
		print "training line size"
	if "testing" in path:
		print "testing line size"
	line_size = []
	for i in range(0,52,4):
		line_size.append([i,0])
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		# l = 0
		# k = 0
		# print lines_f.split()
		for k in range(0,len(lines_f)):
			line = lines_f[k].split()
			for kk in range(len(line_size)):
				if line_size[kk][0] < len(line):
					line_size[kk][1] += 1
		a = []
		for p in range(len(line_size)):
			if line_size[p][1] != 0:
				a.append(math.log(line_size[p][1]))
			else:
				a.append(line_size[p][1])
		writefeatures(each, a)

def leading_space(name_list):
	if "training" in path:
		print "training leading space"
	if "testing" in path:
		print "testing leading space"
	leading_space = []
	for i in range(0,20,4):
		leading_space.append([i,0])
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		for k in range(0,len(lines_f)):
			p = 0 
			try:
				while(lines_f[k][p] == ' '):
					p += 1
			except:
				continue

			for kk in range(len(leading_space)):
				if leading_space[kk][0] < p:
					leading_space[kk][1] += p
		a = []
		for q in range(len(leading_space)):
			if leading_space[q][1] != 0:
				a.append(math.log(leading_space[q][1]))
			else:
				a.append(leading_space[q][1])
		writefeatures(each, a)

def underline(name_list):
	if "training" in path:
		print "training underline"
	if "testing" in path:
		print "testing underline"
	leading_space = []
	for i in range(0,20,2):
		leading_space.append([i,0])
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		for k in range(len(lines_f)):
			p = lines_f.count("_")
			for kk in range(len(leading_space)):
				if leading_space[kk][0] < p:
					leading_space[kk][1] += p
		a = []
		for q in range(len(leading_space)):
			if leading_space[q][1] != 0:
				a.append(math.log(leading_space[q][1]))
			else:
				a.append(leading_space[q][1])
		writefeatures(each, a)

def commas(name_list):
	if "training" in path:
		print "training commas"
	if "testing" in path:
		print "testing commas"
	leading_space = []
	for i in range(0,6,1):
		leading_space.append([i,0])
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		for k in range(len(lines_f)):
			p = lines_f.count(",")
			for kk in range(len(leading_space)):
				if leading_space[kk][0] < p:
					leading_space[kk][1] += p
		a = []
		for q in range(len(leading_space)):
			if leading_space[q][1] != 0:
				a.append(math.log(leading_space[q][1]))
			else:
				a.append(leading_space[q][1])
		writefeatures(each, a)

def semicolons(name_list):
	if "training" in path:
		print "training semicolons"
	if "testing" in path:
		print "testing semicolons"
	leading_space = []
	for i in range(0,6,1):
		leading_space.append([i,0])
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		for k in range(len(lines_f)):
			p = lines_f.count(";")
			for kk in range(len(leading_space)):
				if leading_space[kk][0] < p:
					leading_space[kk][1] += p
		a = []
		for q in range(len(leading_space)):
			if leading_space[q][1] != 0:
				a.append(math.log(leading_space[q][1]))
			else:
				a.append(leading_space[q][1])
		writefeatures(each, a)

def token(name_list):
	if "training" in path:
		print "training token"
	if "testing" in path:
		print "testing token"
	leading_space = []
	for i in range(0,20,2):
		leading_space.append([i,0])
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		for k in range(len(lines_f)):
			p = 0
			for char in lines_f[k]:
				if char > 'a' and char < 'z' or char > 'A' and char < 'Z':
					pass
				elif 0 <= char <= 9:
					pass
				else:
					p += 1

			for kk in range(len(leading_space)):
				if leading_space[kk][0] < p:
					leading_space[kk][1] += p
		a = []
		for q in range(len(leading_space)):
			if leading_space[q][1] != 0:
				a.append(math.log(leading_space[q][1]))
			else:
				a.append(leading_space[q][1])
		writefeatures(each, a)



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
		line_size(name_list)
		leading_space(name_list)
		underline(name_list)
		commas(name_list)
		semicolons(name_list)
		token(name_list)

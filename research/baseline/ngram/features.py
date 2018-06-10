#!/usr/local/bin/python
# coding:utf-8

import os
from os.path import join, getsize
import re
import math
import time
from ShowProcess import ShowProcess
import nltk
from nltk.util import ngrams
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

def word_grams(words, min, max):
	s = []
	for n in range(min,max):
		for ngram in ngrams(words, n):
			s.append(''.join(str(i) for i in ngram))
	return s

def line_size(name_list):
	if "training" in path:
		print "training line size"
	if "testing" in path:
		print "testing line size"

	process_bar = ShowProcess(len(name_list)-1)
	min_s = 10000000
	for each in name_list:
		# print each
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		# print each
		data = readfile(os.path.join(path, each))
		# print data
		data = data.split(' ')
		print data
		# print len(data)
		a = []
		for i in range(0,len(data)):
			if data[i] != ' ':
				if data[i] != '\n':
					a.append(data[i])

		seg = word_grams(a, 7, 8)
		if min_s > len(seg):
			min_s = len(seg)

		writefeatures(each, seg)
	print min_s

def frequence(name_list):
	fre = dict()
	if "training" in path:
		print "training line size"
	if "testing" in path:
		print "testing line size"

	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		# print each
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		data = readfile(os.path.join(path, each))
		# print data
		data = data.split('?')
		# print len(data)
		for i in range(len(data)):
			if data[i] not in fre.keys():
				fre[data[i]] = 1
			else:
				fre[data[i]] += 1
		k = []
		v = []
		ind = []
		order = []
		for key in fre.keys():
			k.append(key)
			v.append(fre[key])

		order = sorted(v)
		ind = sorted(range(len(v)),key=lambda k:v[k])
		# print len(ind)
		add = sum(v)
		k = 100
		seg = []
		while k > 0:

			tmp = len(ind) - (100-k) - 1
			try:
				temp = ind[tmp]
			except:
				temp = 0
			if temp == 0:
				seg.append(float(0))
			else:
				seg.append(float(float(add)/float(v[tmp])))
			k -= 1

		writefeatures(each, seg)

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
			path = "./testingw"
		else:
			path = "./trainingw"
		name_list = get_name(path)
		# line_size(name_list)
		frequence(name_list)

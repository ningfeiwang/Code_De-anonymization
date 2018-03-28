#!/usr/local/bin/python
# coding:utf-8

import os
import re
import math
from langdetect import detect
from langdetect import detect_langs

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def readfile(filename):
	with open(filename) as file:
		data = file.read()
	return data

def writefeatures(label,features):
	name = label.split(".")[0] + ".txt"
	f = open(os.path.join("features",name), 'a')
	for i in range(0,len(features)):
		f.write(str(features[i]))
		f.write(",")
	# f.write(data)
	# f.write('\n')
	f.close()

def keywords(name_list):
	key_word = readfile("python_keyword.txt")
	key_word = key_word.split("\n")
	fea = dict()

	for each in name_list:
		if each == ".DS_Store":
			continue
		for k in key_word:
			fea[k] = 0
		l = 0
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		# print lines_f
		f.close()
		for line in lines_f:
			# if "#" in 
			l += len(line.split(" "))
			for k in fea.keys():
				if "#" in line:
					a = line.split("#")[0].count(k)
				else:
					a = line.count(k)
				fea[k] += a
		print l
		for k in fea.keys():
			if fea[k] == 0:
				fea[k] = 1
			else:
				fea[k] = math.log(float(l/fea[k]))
		list_fea = []
		for k in key_word:
			list_fea.append(fea[k])
		writefeatures(each,list_fea)

def detect_lang(name_list):
	language = dict()
	result = dict()
	language["en"] = 0
	for each in name_list:
		if each == ".DS_Store":
			continue
		# lan = "a"
		det_lan = []
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		# print lines_f
		f.close()
		print each
		for i in range(0,len(lines_f)):
			if "#" in lines_f[i]:
				a = lines_f[i].split("#")[-1]
				try:
					
					lan = detect(a)
					if lan == 'en':
						continue
					else:
						det_lan.append(lan)
					if lan not in language:
						language[lan] = len(language.keys())*100
						# serial.append(len(language)*100)

				except:
					continue
		if len(det_lan) == 0:
			result[each] = 0
		else:
			result[each] = 0
			for t in range(0, len(det_lan)):
				result[each] += language[det_lan[t]]
		print result
		writefeatures(each,[math.log(float(result[each]))])

def nums_function(name_list):
	nums = {}
	for each in name_list:
		data = readfile(os.path.join(path,each))
		nums[each] = data.count("def")
		print nums
		writefeatures(each,[math.log(float(nums[each]))])

def nums_lenline(name_list):
	lenline = {}
	for each in name_list:
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		l = 0
		k = 0
		for i in range(0, len(lines_f)):
			if "#" in lines_f[i]:
				lines_f[i] = lines_f[i].split("#")[0]
			if lines_f[i] == "":
				continue
			k += 1
			line = lines_f[i].split(" ")
			for j in range(0,len(line)):
				if line[j] != " ":
					l += 1 
		lenline[each] = float(l/k)
		print lenline
		writefeatures(each, [lenline[each]])

def comment_len(name_list):
	comment = {}
	for each in name_list:
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		l = 0
		k = 0
		com = 0
		for i in range(0, len(lines_f)):
			if "#" in lines_f[i]:
				com += 1
				lines_f[i] = lines_f[i].split("#")[-1]
			# if lines_f[i] == "":
			# 	continue
			k += 1
			line = lines_f[i].split(" ")
			for j in range(0,len(line)):
				if line[j] != " ":
					l += 1 
		comment[each] = [float(l/k), math.log(float(k/com))]
		print comment
		writefeatures(each, comment[each])


if __name__ == '__main__':
	global path
	path = '/Users/ningfeiwang/Documents/spring2018/cse498_info_privacy/project/Code_De-anonymization/dataset/features/data_sum'
	name_list = get_name(path)
	# keywords(name_list)
	# detect_lang(name_list)
	# nums_function(name_list)
	# nums_lenline(name_list)
	# comment_len(name_list)
	
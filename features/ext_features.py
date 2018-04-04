#!/usr/local/bin/python
# coding:utf-8

import os
import re
import math
from langdetect import detect
from langdetect import detect_langs
import time
from ShowProcess import ShowProcess
import ast
import ast_visit

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
	name = label.split(".")[0] + ".txt"
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

def keywords(name_list):
	key_word = readfile("python_keyword.txt")
	key_word = key_word.split("\n")
	fea = dict()
	if "training" in path:
		print "training keywords"
	if "testing" in path:
		print "testing keywords"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
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
		# print l
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
	if "training" in path:
		print "training language"
	if "testing" in path:
		print "testing language"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		# lan = "a"
		det_lan = []
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		# print lines_f
		f.close()
		# print each
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
		# print result
		if result[each] != 0:
			writefeatures(each,[math.log(float(result[each]))])
		else:
			writefeatures(each,[float(result[each])])


def nums_function(name_list):
	nums = {}
	if "training" in path:
		print "training functions"
	if "testing" in path:
		print "testing functions"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		data = readfile(os.path.join(path,each))
		nums[each] = data.count("def")
		# print nums
		if nums[each] != 0:
			writefeatures(each,[math.log(float(nums[each]))])
		else:
			writefeatures(each,[float(nums[each])])

def nums_lenline(name_list):
	lenline = {}
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
		# q = float(l/k)
		# l = 0
		# k = 0
		# lk = 0
		# for i in range(0, len(lines_f)):
		# 	if "#" in lines_f[i]:
		# 		lines_f[i] = lines_f[i].split("#")[0]
		# 	if lines_f[i] == "":
		# 		continue
		# 	k += 1
		# 	line = lines_f[i].split(" ")
		# 	for j in range(0,len(line)):
		# 		if line[j] != " ":
		# 			l += 1
		# 	lk += (l - q) ** 2
		# lk = lk/k
		lenline[each] = [float(l/k)]
		# print lenline
		writefeatures(each, lenline[each])

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
		if k == 0:
			k = 1
		if com == 0:
			com = 1
		comment[each] = [float(l/k), math.log(float(k/com))]
		# print comment
		writefeatures(each, comment[each])

def check_space(name_list):
	# space = dict()
	if "training" in path:
		print "training space between string"
	if "testing" in path:
		print "testing space between string"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		data = readfile(os.path.join(path,each))
		# equ_nums = data.count("=")
		# clean_nums = data.count("==") + data.count("!=")
		equ_nums_space = data.count(" = ")
		# real_equ = equ_nums - clean_nums
		if equ_nums_space > 2:
			# print 1
			writefeatures(each, [float(1)])
		else:
			writefeatures(each, [float(0)])

def par_nums(name_list):
	# space = dict()
	if "training" in path:
		print "training parameter number"
	if "testing" in path:
		print "testing parameter number"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		l = 0
		k = 0
		for i in range(0, len(lines_f)):
			if "def" in lines_f[i]:
				par_nums = re.findall(r'(.*)', lines_f[i])[0].count(",") + 1
				l += 1
				k += par_nums
		if l == 0:
			writefeatures(each, [float(0)])
			# print 0
		else:
			writefeatures(each, [float(k/l)])
			# print 1
def empty_line(name_list):
	if "training" in path:
		print "training empty lines"
	if "testing" in path:
		print "testing empty lines"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		l = 0
		k = 0
		for i in range(0, len(lines_f)):
			if lines_f[i].strip() == "":
				l += 1
			k += 1
		if l == 0:
			writefeatures(each, [float(0)])
		else:
			writefeatures(each, [float(k/l)])

def import_num(name_list):
	if "training" in path:
		print "training import"
	if "testing" in path:
		print "testing import"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		l = 0
		k = 0
		for i in range(0, len(lines_f)):
			k += 1
			if "#" in lines_f[i]:
				if "import" in lines_f[i].split("#")[0]:
					l += 1
			else:
				if "import" in lines_f[i]:
					l += 1
		if l == 0:
			# print [0]
			writefeatures(each, [0])
		else:
			# print l
			writefeatures(each, [l])

def from_import(name_list):
	if "training" in path:
		print "training from import and import as"
	if "testing" in path:
		print "testing from import and import as"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		l = 0
		p = 0
		k = 0
		for i in range(0, len(lines_f)):
			k += 1
			if "#" in lines_f[i]:
				l += len(re.findall(r'from .* import .*', lines_f[i].split("#")[0]))
				p += len(re.findall(r'import .* as .*', lines_f[i].split("#")[0]))
			else:
				l += len(re.findall(r'from .* import .*', lines_f[i]))
				p += len(re.findall(r'import .* as .*', lines_f[i]))
		if l == 0:
			# print [0]
			writefeatures(each, [0,0])
		else:
			# print l
			writefeatures(each, [l,p])

def coding(name_list):
	if "training" in path:
		print "training coding"
	if "testing" in path:
		print "testing coding"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		flag1 = float(0)
		flag2 = float(0)
		flag3 = float(0)
		for i in range(0, len(lines_f)):
			if "UTF-8" in lines_f[i]:
				flag1 = float(1)
			if "#!/usr/bin/" in lines_f[i]:
				flag2 = float(1)
			if "python2" in lines_f[i]:
				flag3 = float(1)
			elif "python3" in lines_f[i]:
				flag3 = float(2)
		writefeatures(each, [flag1, flag2, flag3])

def print_sty(name_list):
	if "training" in path:
		print "training print style"
	if "testing" in path:
		print "testing print style"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		flag = float(0)
		for i in range(0, len(lines_f)):
			if "#" in lines_f[i]:
				if "print" in lines_f[i].split("#")[0]:
					if "(" not in lines_f[i].split("#")[0]:
						if ")" not in lines_f[i].split("#")[0]:
							flag = float(1)
					if lines_f[i].split("#")[0].count("(") == 1:
						flag = float(2)
			else:
				if "print" in lines_f[i]:
					if "(" not in lines_f[i]:
						if ")" not in lines_f[i]:
							flag = float(1)
					if lines_f[i].count("(") == 1:
						flag = float(2)
		# print each
		# print flag
		writefeatures(each, [flag])

def test_function(name_list):
	if "training" in path:
		print "training test function"
	if "testing" in path:
		print "testing test function"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		flag = 0
		for i in range(0, len(lines_f)):
			if "if __name__ == '__main__'" in lines_f[i]:
				flag = 1
		writefeatures(each, [float(flag)])
		# print flag

def tab_spa(name_list):
	if "training" in path:
		print "training tab and space"
	if "testing" in path:
		print "testing tab and space"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		flag = 0
		# print each
		for i in range(0, len(lines_f)):
			if ":" in lines_f[i]:
				if "\t" in lines_f[i+1]:
					flag = 1
					break
				else:
					flag = 0
					break
		writefeatures(each, [float(flag)])

		# print flag

def ast_nodenums(name_list):
	key_word = readfile("ast_nodetype.txt")
	key_word = key_word.split("\n")
	if "training" in path:
		print "training ast node nums"
	if "testing" in path:
		print "testing ast node nums"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		try:
			tree = ast.parse(open(os.path.join(path,each)).read())
		except:
			writefeatures(each, [float(0)])
			for k in (0,len(key_word)):
				writefeatures(each, [math.log(float(1))])
			continue
		x = ast_visit.visit()
		x.visit(tree)
		f = open("ast.txt",'r')
		lines_f = f.readlines()
		f.close()
			# continue:


		# print len(lines_f[0].split(","))
		# print math.log(len(lines_f[0].split(",")))
		# print len(lines_f[0].split(","))
		writefeatures(each, [math.log(len(lines_f[0].split(",")))])
		# print 111111
		kk = get_length(each)
		print kk
		# break
		os.system("rm ast.txt")
		lines = lines_f[0].split(",")
		for i in range(0,len(lines)):
			for k in key_word:
				lines.count(k)
				if len(lines_f[0].split(",")) == 0:
					writefeatures(each, [math.log(float(1))])
				else:
					# print kk 
					# print len(lines_f[0].split(","))
					# if kk > len(lines_f[0].split(",")):
					# 	writefeatures(each, [float(0.1)])
					# else:
					writefeatures(each, [float(len(lines_f[0].split(","))/kk)])



if __name__ == '__main__':
	global path
	os.system("mkdir trainingfeature")
	os.system("mkdir testingfeature")
	
	for i in range(0,2):
		if i == 0:
			path = '/Users/ningfeiwang/Documents/spring2018/cse498_info_privacy/project/Code_De-anonymization/dataset/classification/testing'
		else:
			path = '/Users/ningfeiwang/Documents/spring2018/cse498_info_privacy/project/Code_De-anonymization/dataset/classification/training'
		name_list = get_name(path)
		keywords(name_list)
		# detect_lang(name_list)
		nums_function(name_list)
		nums_lenline(name_list)
		comment_len(name_list)
		check_space(name_list)
		par_nums(name_list)
		empty_line(name_list)
		import_num(name_list)
		from_import(name_list)
		coding(name_list)
		print_sty(name_list)
		test_function(name_list)
		tab_spa(name_list)
		ast_nodenums(name_list)
		

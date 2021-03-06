#!/usr/local/bin/python
# coding:utf-8

import os
import re
import math
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
				fea[k] = math.log(float(float(l)/float(fea[k])))
		list_fea = []
		for k in key_word:
			list_fea.append(float(fea[k]))
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
		nums[each] = [data.count("def"),data.count("class")]
		# print nums
		if nums[each][0] != 0:
			writefeatures(each,[math.log(float(nums[each][0])),float(nums[each][1])])
		else:
			writefeatures(each,[float(nums[each][0]),float(nums[each][1])])

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
		lenline[each] = [float(float(l)/float(k))]
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
		comment[each] = [float(float(l)/float(k)), math.log(float(float(k)/float(com)))]
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
			writefeatures(each, [float(float(k)/float(l))])
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
			writefeatures(each, [float(float(k)/float(l))])

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
			writefeatures(each, [float(0),math.log(float(1)),math.log(float(1)),math.log(float(1)),math.log(float(1)),math.log(float(1)),math.log(float(1)),math.log(float(1))])
			# for k in (0,len(key_word)):
			# 	writefeatures(each, [math.log(float(1))])

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
		writefeatures(each, [math.log(float(len(lines_f[0].split(","))))])
		# print 111111
		kk = get_length(each)
		# print kk
		# break
		os.system("rm ast.txt")
		lines = lines_f[0].split(",")
		# for i in range(0,len(lines)):
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
				writefeatures(each, [float(float(len(lines_f[0].split(",")))/float(kk))])

def len_parAfor(name_list):
	if "training" in path:
		print "training ast node nums"
	if "testing" in path:
		print "testing ast node nums"
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
		for i in range(0, len(lines_f)):
			if "for" in lines_f[i]:
				line = lines_f[i].split()
				for k in range (0,len(line)):
					if line[k] == "for":
						break
				p += 1
				if k+1 == len(line):
					continue
				else:
					l += len(line[k+1])
		if p == 0:
			# print p
			writefeatures(each,[float(0)])
		else:
			# print float(float(l)/p)
			writefeatures(each,[float(float(l)/p)])



def ifforinline(name_list):
	# pass
	if "training" in path:
		print "training ast node nums"
	if "testing" in path:
		print "testing ast node nums"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		# flag = 0
		l = 0
		k = 0
		for i in range(0, len(lines_f)):
			if "for" in lines_f[i]:
				line = lines_f[i].split()
				if "for" != line[0]:
					l += 1
					# l = 0
			k += 1
		# print float(float(l)/k)
		writefeatures(each,[float(float(l)/k)])



def xhxuse(name_list):
	if "training" in path:
		print "training ast node nums"
	if "testing" in path:
		print "testing ast node nums"
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
		flag = 0
		for i in range(0, len(lines_f)):
			if "for" in lines_f[i]:
				# pass
				line = lines_f[i].split()
				for kk in range(0, len(line)):
					if line[kk] == "for":
						break
				if kk + 1 == len(line):
					continue
				if "_" in line[kk+1]:
					l += 1
					flag = 1
			k += 1
		# print float(float(l)/k)
		writefeatures(each,[float(float(l)/k), float(flag)])

def lower_chars(string):
	return sum(map(str.islower, string))

def upper_chars(string):
	return sum(map(str.isupper, string))

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
			writefeatures(each, [float(0),float(0),float(0),float(0), float(0)]) #big first, big num and _ nums, li nums
			continue

		names = sorted({node.id for node in ast.walk(root) if isinstance(node, ast.Name)})
		big_num = 0
		un_num = 0
		big_fir = 0
		low_num = 0
		str_fir = 0
		if len(names) == 0:
			writefeatures(each, [float(0),float(0),float(0),float(0), float(0)]) #big first, big num and _ nums, li nums
			continue
		for i in range(0, len(names)):
			un_num += names[i].count("_")
			big_num += upper_chars(names[i])
			low_num += lower_chars(names[i])
			if names[i][0].isupper():
				big_fir += 1
			elif names[i][0].islower():
				pass
			else:
				str_fir += 1

		writefeatures(each, [float(float(big_num)/float(len(names))),float(float(un_num)/float(len(names))),float(float(big_fir)/float(len(names))),float(float(low_num)/float(len(names))),float(float(str_fir)/float(len(names)))])

def len_fun(name_list):
	# nums = {}
	if "training" in path:
		print "training len function"
	if "testing" in path:
		print "testing len function"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		num = 0
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		data = readfile(os.path.join(path,each))
		num = data.count("def")
		f = open(os.path.join(path,each),'r')
		lines_f = f.readlines()
		f.close()
		j = 0
		len_fun = 0
		flag = 0
		for i in range(0, len(lines_f)):
			if "def" in lines_f[i]:
				j += 1
				flag = 1
			if j >= num:
				flag = 0
			if flag == 1:
				len_fun += 1

		if len_fun == 0:
			writefeatures(each, [float(0)])
		elif num == 0:
			writefeatures(each, [float(0)])
		else:
			writefeatures(each, [float(math.log(float(len_fun)/float(num)))])















# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& dynamic features

def run_code(name_list):
	if "training" in path:
		print "training par"
	if "testing" in path:
		print "testing par"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		prob = each.split("_")[0][1:]
		if "training" in path:
			cmd = "nohup python -m cProfile " + "./training/" + each + "< ./sample_input/" + prob + ".txt"+ ">./traininglog/" + each + ".txt" + " 2>&1 &"
			print cmd
			os.system(cmd)
			cmd = "rm *.out"
			os.system(cmd)
		else:
			# cmd = "nohup python " + "./testing/" 
			cmd = "nohup python -m cProfile " + "./testing/" + each + "< ./sample_input/" + prob + ".txt"+ ">./testinglog/" + each + ".txt" + " 2>&1 &"
			print cmd
			os.system(cmd)
			cmd = "rm *.out"
			os.system(cmd)

		# nohup python3 model_train.py > yeu.log 2>&1 &

def get_callfunnums():
	if "training" in path:
		a = "traininglog"
		print "training par"
	if "testing" in path:
		a = "testinglog"
		print "testing par"

	p = "./"+a
	name_list = get_name(p)
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		name = each.split(".txt")[0]
		p = "./" + a +"/"+ each
		f = open(p,'r')
		lines_f = f.readlines()
		f.close()
		module_time = 0
		calls = 0
		times = 0
		abo_100 = 0
		abo_50 = 0
		abo_10 = 0
		equ_1 = 0
		flag = 0
		mul_num = 0
		content = readfile(p)
		if "error" in content:
			writefeatures(each,[float(calls),float(times),float(abo_100),float(abo_50),float(abo_10),float(equ_1),float(module_time)])
			continue
		if "Error" in content:
			writefeatures(each,[float(calls),float(times),float(abo_100),float(abo_50),float(abo_10),float(equ_1),float(module_time)])
			continue
		for line in lines_f:
			try:
				# if "function calls" in line:
					# calls = line.split()[0]
				if "function calls" in line:
					for i in range(0,len(line.split())-1):
						if line.split()[i] == 'function':
							if line.split()[i+1] == "calls":
								calls = line.split()[i-1]
					# calls = line.split()[0]
					times = line.split()[-2]
				else:
					if line.split()[0] == "ncalls":
						flag = 1
						continue
				if flag == 1:
					if int(line.split()[0]) >= 100:
						abo_100 += 1
					elif int(line.split()[0]) >= 50:
						abo_50 += 1
					elif int(line.split()[0]) >= 10:
						abo_10 += 1
					else:
						if int(line.split()[0]) == 1:
							equ_1 += 1

				if "<module>" in line:
					mul_num += 1
					module_time += line.split()[3]
			except:
				continue
		if mul_num != 0:
			module_time = float(module_time) / float(mul_num)
		if calls == 0:

			writefeatures(each,[float(calls),float(times),float(abo_100),float(abo_50),float(abo_10),float(equ_1),float(module_time)])
		else:
			writefeatures(each,[float(math.log(float(calls))),float(times),float(abo_100),float(abo_50),float(abo_10),float(equ_1),float(module_time)])
				# input-content label-is-hidden style-scope paper-input-container

 	# 489 function calls in 0.006 seconds

  #  Ordered by: standard name

  #  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #       1    0.000    0.000    0.000    0.000 StringIO.py:30(<module>)
  #       1    0.000    0.000    0.000    0.000 StringIO.py:42(StringIO)
  #       1    0.000    0.000    0.000    0.000 UserDict.py:4(__init__)
  #       1    0.000    0.000    0.000    0.000 __init__.py:1010(Manager)
  #       1    0.000    0.000    0.000    0.000 __init__.py:1015(__init__)
  #       1    0.000    0.000    0.000    0.000 __init__.py:1112(Logger)
  #       1    0.000    0.000    0.000    0.000 __init__.py:1127(__init__)
  #       1    0.000    0.000    0.000    0.000 __init__.py:1139(setLevel)
  #       1    0.000    0.000    0.000    0.000 __init__.py:1298(addHandler)
def run_memcode(name_list):
	os.system("rm -rf trainingmemlog")
	os.system("rm -rf testingmemlog")
	os.system("mkdir trainingmemlog")
	os.system("mkdir testingmemlog")
	if "training" in path:
		print "training run mem"
	if "testing" in path:
		print "testing run mem"
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		prob = each.split("_")[0][1:]
# python -m memory_profiler ShowProcess.py
		if "training" in path:
			cmd = "nohup python -m memory_profiler " + "./training/" + each + "< ./sample_input/" + prob + ".txt"+ ">./trainingmemlog/" + each + ".txt" + " 2>&1 &"
			print cmd
			os.system(cmd)
			# cmd = "echo $!"
			# a = os.system(cmd)
			# time.sleep(3)
			# cmd = "kill -9 " + a
			# os.system(cmd)
			# cmd = "rm *.out"
			# os.system(cmd)
		else:
			# cmd = "nohup python " + "./testing/" 
			cmd = "nohup python -m memory_profiler " + "./testing/" + each + "< ./sample_input/" + prob + ".txt"+ ">./testingmemlog/" + each + ".txt" + " 2>&1 &"
			print cmd
			os.system(cmd)
			# cmd = "rm *.out"
			# os.system(cmd)


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     35   32.594 MiB    0.000 MiB   @profile
#     36                             def main():
#     37   32.594 MiB    0.000 MiB       if len(sys.argv) > 1:
#     38                                     return doit()
#     39
#     40   32.594 MiB    0.000 MiB       compileIfNeeded()


def mem_fea():
	if "training" in path:
		a = "trainingmemlog"
		print "training par"
	if "testing" in path:
		a = "testingmemlog"
		print "testing par"
	p = "./"+a
	name_list = get_name(p)
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		name = each.split(".txt")[0]
		p = "./" + a +"/"+ each
		f = open(p,'r')
		lines_f = f.readlines()
		f.close()
		num = 0
		mem = 0.0
		#                 mem = 0.0
  #               for k in range(0, len(lines_f)):
  #                       if "@profile" in lines_f[k]:
  #                               try:
  #                                   mem += float(lines_f[k].split()[1])
  #                                   num += 1
  #                               except:
  #                                   continue

  #               if mem == 0.0:
		for k in range(0, len(lines_f)):
			if "@profile" in lines_f[k]:
				try:
					mem += float(lines_f[k].split()[1])
					num += 1
				except:
					continue

		if mem == 0.0:
			writefeatures(each,[float(mem)])
		elif num == 0:
			writefeatures(each,[float(num)])
		else:
			writefeatures(each,[float(math.log(float(mem)/float(num)))])
				# input-content label-is-hidden style-scope paper-input-container

def mem_val():
	if "training" in path:
		a = "trainingdis"
		print "training dis"
	if "testing" in path:
		a = "testingdis"
		print "testing dis"
	p = "./"+a
	name_list = get_name(p)
	process_bar = ShowProcess(len(name_list)-1)
	for each in name_list:
		process_bar.show_process()
		if each == ".DS_Store":
			continue
		name = each.split(".txt")[0]
		p = "./" + a +"/"+ each
		f = open(p,'r')
		lines_f = f.readlines()
		f.close()
		tmp = []
		for i in range(0,len(lines_f)):
			if "STORE_NAME" in lines_f[i]:
				tmp.append([lines_f[i].split()[2],lines_f[i].split()[3]])
		if len(tmp) == 0:
			writefeatures(each,[float(len(tmp)),float(len(tmp)),float(len(tmp)),float(len(tmp)),float(len(tmp)),float(len(tmp)),float(len(tmp)),float(len(tmp))])
			continue
		temp = dict()
		for i in range(0, len(tmp)):
			if tmp[i][0] in temp.keys():
				temp[tmp[i][0]].append(tmp[i][1])
			else:
				temp[tmp[i][0]] = [tmp[i][1]]
		dis_mem = len(temp.keys())
		max_num = 0
		min_num = 1000
		ave = 0.0
		sum_num = 0
		les_10 = 0
		abo_10 = 0
		abo_20 = 0
		abo_40 = 0
		for key in temp.keys():
			sum_num += len(temp[key])
			if min_num > len(temp[key]):
				min_num = len(temp[key])
			if max_num < len(temp[key]):
				max_num = len(temp[key])
			if len(temp[key]) < 10:
				les_10 += 1
			if len(temp[key]) > 10:
				abo_10 += 1
			if len(temp[key]) > 20:
				abo_20 += 1
			if len(temp[key]) > 40:
				abo_40 += 1
		ave = float(sum_num)/float(len(temp.keys()))
		writefeatures(each,[float(dis_mem),float(max_num),float(min_num),float(ave),float(les_10),float(abo_10),float(abo_20),float(abo_40)])

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
		# f = open('./trainingname.txt','r')
		# lines_f = f.readlines()
		# f.close()
		# j = 0
		# name_list = []
		# for kkk in lines_f:
		# 	if j > 500:
		# 		continue
		# 	name_list.append(kkk)
		# 	j += 1
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
		len_parAfor(name_list)
		ifforinline(name_list)
		xhxuse(name_list)
		get_par(name_list)
		len_fun(name_list)
# &&&&&&&&&&&&&&&&&&&&&&&&&&&dynamic
		# run_code(name_list)
		get_callfunnums()
		# run_memcode(name_list)
		mem_fea()
		mem_val()

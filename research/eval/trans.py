#!/usr/local/bin/python
# coding:utf-8

import os
import csv

def trans(name_csv, name_txt):
	with open("./train_csv/" + name_csv, 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, dialect='excel')
		# 读要转换的txt文件，文件每行各词间以@@@字符分隔
		with open(path + "/" + name_txt, 'rb') as filein:
			for line in filein:
				line_list = line.strip('\n').split(',')
				spamwriter.writerow(line_list)


def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def get_data(path, x, y, label):
	name_list = get_name(path)
	# data1 = readfile(os.path.join(path, name_list[0]))
	# data1 = data1.split(",")
	# print data
	# data1.pop()
	# ori = len(data1)
	# print (ori)
	for each in name_list:
		if each == ".DS_Store":
		    continue
		a = each.split("_")[1]
		trans(each +  '$' + str(label[a]) + "$" + '.csv', each)
	
if __name__ == '__main__':
	global path
	path = './trainingfeature'
	os.system("rm -rf train_csv")
	os.system("mkdir train_csv")
	label = dict()
	name_list = get_name(path)
	p = 0
	for i in range(0,len(name_list)):
		if name_list[i] == ".DS_Store":
			continue
		a = name_list[i].split("_")[1]
		if a in label.keys():
			continue

		label[a] = p
		p += 1
	y = []
	x = []
	get_data(path, x, y, label)
	# os.system("rm -rf test_csv")
	# os.system("mkdir test_csv")
	# global path
	# path = './testingfeature'
	# name_list = get_name(path)
	# for each in name_list:
	# 	if (each == '.DS_Store'):
	# 		continue
		# trans(each.split('.txt')[0] + '.csv',each)
		
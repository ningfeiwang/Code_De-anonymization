#!/usr/local/bin/python
# coding:utf-8

import os
from os.path import join, getsize
import re
import math
import time

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

if __name__ == '__main__':
	global path
	path = './new_data'
	name_list = get_name(path)
	res = []
	pro = []
	for each in name_list:
		name = each.split('.py')[0].split('_')
		# if int(name[-1]) > 54:
		res.append(name[1])
		pro.append(name[0])
	no_re = []
	no_pro = []
	for i in range(len(res)):
		if res[i] not in no_re:
			no_re.append(res[i])
	for i in range(len(pro)):
		if pro[i] not in no_pro:
			no_pro.append(pro[i])
	print len(no_re)
	print len(no_pro)
	print len(name_list)



	# global path
	# path = './data'
	# name_list = get_name(path)
	# usr = ['xjcl', 'Sp3000', 'dpforest', 'alexwice', 'bigOnion', 'caethan', 'RalfKistner', 'kmod', 'gizzywump', 'addie9000', 'SergGr', 'urupica', 'tpablo', 'waitingkuo0527', 'MichelJ', 'Michael', 'royf', 'd.operator', 'FatAlex', 'Jethol', 'graygrass', 'IdoLivneh', 'mth']


	# pro = ['p5756407898963968', 'p5634697451274240', 'p5686275109552128', 'p5636311922769920', 'p5639104758808576', 'p5738606668808192', 'p2453486', 'p5652388522229760', 'p5709773144064000']
	# os.system('rm -rf new_data')
	# os.system('mkdir new_data')
	# for each in name_list:
	# 	name = each.split('.py')[0].split('_')
	# 	if name[0] in pro:
	# 		if name[1] in usr:
	# 			cmd = 'cp ./data/' + each + ' ./new_data'
	# 			os.system(cmd)

	# pro = dict()
	# p = 0
	# for each in name_list:
	# 	name = each.split('.py')[0].split('_')
	# 	if name[0] not in pro.keys():
	# 		pro[name[0]] = 0
	# 	else:
	# 		pro[name[0]] += 1

	# p = []
	# for key in pro.keys():
	# 	if pro[key] > 48:
	# 		p.append(key)
	# print p



	# usr = {}
	# u = []
	# for each in name_list:
	# 	name = each.split('.py')[0].split('_')
	# 	if name[1] not in usr.keys():
	# 		usr[name[1]] = [name[0]]
	# 	else:
	# 		usr[name[1]].append(name[0])
	# # flag = 0
	# # print usr
	# for key in usr.keys():
	# 	flag = 0
	# 	for i in range(len(pro)):
	# 		if pro[i] in usr[key]:
	# 			flag = 1
	# 			continue
	# 		else:
	# 			flag = 0
	# 			break
	# 	if flag == 1:
	# 		u.append(key) 
	# print u[0:23]



	# 	if name[1] not in usr:
	# 		usr.append(name[1])
	# 		if len(usr) > 22:
	# 			break
	# 	if name[0] not in pro:
	# 		pro.append(name[0])
	# 		if len(pro) > 8:
	# 			break
	# print len(usr)
	# print pro
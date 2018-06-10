#!/usr/local/bin/python
# coding:utf-8

import os
import math
import copy

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def readfile(filename):
	with open(filename) as file:
		data = file.read()
	return data

def get_data(path, x, y, label):
	name_list = get_name(path)
	data1 = readfile(os.path.join(path, name_list[0]))
	data1 = data1.split(",")
	# print data
	data1.pop()
	ori = len(data1)
	for each in name_list:
		if each == ".DS_Store":
			continue
		data = readfile(os.path.join(path, each))
		data = data.split(",")
		# print data
		data.pop()
		l = len(data)
		# data.pop(33)
		for k in range(0, len(data)):
			data[k] = float(data[k])
			# trainx.append()
		if l == ori:
			x.append(data)
			a = each.split("_")[1]
			# try:
			y.append([label[a]])

def distance(x,y):
	tmp = 0
	for i in range(len(x)):
		tmp += abs(x[i] - y[i]) ** 2
	return math.sqrt(tmp)

def prediction(trainx,trainy,testx):
	predict_y = []
	for test in testx:
		dis = []
		tmp = []
		for train in trainx:
			dis.append(distance(test,train))
		for kk in range(len(dis)):
			if dis[kk] != 0:
				tmp.append(dis[kk])
			
		index = sorted(range(len(tmp)),key=lambda x:tmp[x])
                sor = sorted(tmp)
                # temp = 10000000.0
		ind = []
		t = []
                p = 0
		for i in range(0,70):
		    ind.append(index[i])
		for i in range(0,7):
                    pp = 0
                    for kk in range(0,len(t)):
                        if t[kk] == trainy[ind[i]]:
                            while True:
                                if t[kk] == trainy[ind[pp+i]]:
                                    pp += 1
                                    continue
                                else:
                                    break


                        
		    t.append(trainy[ind[i+pp]])
		predict_y.append(t)

	return predict_y

def cal_score(x, y):
	point = 0
	for i in range(len(x)):
		for j in range(len(y[i])):
			if x[i] == y[i][j]:
				point += 4
	return float(float(point)/ float(len(x)))

if __name__ == '__main__':

	path_train = './trainingfeature'
	path_test = './testingfeature'
	testx = []
	testy = []
	trainx = []
	trainy = []
	label = dict()
	name_list = get_name(path_train)
	p = 0
	for i in range(0,len(name_list)):
		if name_list[i] == ".DS_Store":
			continue
		a = name_list[i].split("_")[1]
		if a in label.keys():
			continue
		# else:
		label[a] = p
		p += 1

	get_data(path_train, trainx, trainy, label)

	get_data(path_test, testx, testy, label)

	y_pred = prediction(trainx,trainy,testx)
	print y_pred
	#print testy
	print len(testy)
	score = cal_score(testy,y_pred)
	print score

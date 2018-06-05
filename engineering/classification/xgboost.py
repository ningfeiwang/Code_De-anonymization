#!/usr/local/bin/python
# coding:utf-8

import os
from xgboost import XGBClassifier
import numpy as np
from sklearn.metrics import accuracy_score


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
		# if len(data) >= 33:
		# 	data.pop(33)
		l = len(data)
		for k in range(0, len(data)):
			data[k] = float(data[k])
			# trainx.append()
		if l == ori:
			x.append(data)
			a = each.split("_")[1]
			y.append([label[a]])
	# print len(x)
	# print y
		# print data
def main(X_train, y_train, X_test, y_test):
	X_train = np.array(X_train)
	X_test = np.array(X_test)
	y_train = np.array(y_train)
	y_test = np.array(y_test)
	model = XGBClassifier()
	model.fit(X_train, y_train)
	y_pred = model.predict(X_test)
	accuracy = accuracy_score(y_test, y_pred)
	print("Accuracy: %.2f%%" % (accuracy * 100.0))


if __name__ == '__main__':
	# global testx, testy, trainx,trainy
	# global path_train, path_test
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

		label[a] = p
		p += 1
	print (p)
	# print len(label)
	get_data(path_train, trainx, trainy, label)
	# print (len(trainx))
	# print (len(trainx[0]))
	get_data(path_test, testx, testy, label)

	main(trainx,trainy,testx,testy)
	

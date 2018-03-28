#!/usr/local/bin/python
# coding:utf-8

import os
import model
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.decomposition import PCA

def get_name(filename):
	name_list = os.listdir(filename)
	return name_list

def readfile(filename):
	with open(filename) as file:
		data = file.read()
	return data

def get_data(path, x, y, label):
	name_list = get_name(path)

	for each in name_list:
		if each == ".DS_Store":
			continue
		data = readfile(os.path.join(path, each))
		data = data.split(",")
		# print data
		data.pop()
		for k in range(0, len(data)):
			data[k] = float(data[k])
			# trainx.append()
		x.append(data)
		y.append([label[each]])
		# print data


if __name__ == '__main__':
	# global testx, testy, trainx,trainy
	# global path_train, path_test
	path_train = '/Users/ningfeiwang/Documents/spring2018/cse498_info_privacy/project/Code_De-anonymization/dataset/classification/trainingfeature'
	path_test = '/Users/ningfeiwang/Documents/spring2018/cse498_info_privacy/project/Code_De-anonymization/dataset/classification/testingfeature'
	testx = []
	testy = []
	trainx = []
	trainy = []
	label = dict()
	name_list = get_name(path_train)
	for i in range(0,len(name_list)):
		if name_list[i] == ".DS_Store":
			continue
		label[name_list[i]] = i
	get_data(path_train, trainx, trainy, label)
	# print trainx

	# print trainy
	get_data(path_test, testx, testy, label)
	# print testx
	# print testy
	clf = model.random_forest_classifier()
	ins = clf.fit(trainx, trainy)
	# res = clf.predict_proba(testx)
	# print res
	print ins.score(testx,testy)

	# name_train = get_name(path_train)
	# name_test = get_name(path_test)























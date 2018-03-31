#!/usr/local/bin/python
# coding:utf-8

import os
import model
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.decomposition import PCA
import numpy as np

def pca_list(x, var):
	res = []
	for i in x:
		cur = []
		for j in range(0,37):
			if var[j] > 0.001:
				cur.append(i[j])
		res.append(cur)
	return res

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
			a = each.split("_")[0]
			y.append([label[a]])
	# print len(x)
	# print y
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
	p = 0
	for i in range(0,len(name_list)):
		if name_list[i] == ".DS_Store":
			continue
		a = name_list[i].split("_")[0]
		if a in label.keys():
			continue

		label[a] = p
		p += 1
	# print len(label)
	get_data(path_train, trainx, trainy, label)
	# l1 = ['b','c','d','b','c','a','a']
	# ll = len(trainx[0])
	# pp = []
	# for i in range(0,len(trainx)):
	# 	if ll != len(trainx[i]):
	# 		# print i
	# 		# print trainx[i]
	# 		pp.append(i)
	# print pp
	# for kkk in pp:
	# 	trainx.pop(kkk - 1)
	# 	trainy.pop(kkk - 1)
	# l2 = []
	# for i in trainy:
	# 	if i not in l2:
	# 		l2.append(i)
	# print len(l2)
	

	# print trainy
	get_data(path_test, testx, testy, label)
	# ll = len(testx[0])
	# pp = []
	# for i in range(0,len(testx)):
	# 	if ll != len(testx[i]):
	# 		# print i
	# 		# print trainx[i]
	# 		pp.append(i)
	# print pp
	# for kkk in pp:
	# 	testx.pop(kkk - 1)
	# 	testy.pop(kkk - 1)

	# print label
	# testx = np.array(testx)
	# trainx = np.array(trainx)
	# testy = np.array(testy)
	# trainy = np.array(trainy)
	# var = PCA(n_components=38, copy=True, 
	# whiten=False, svd_solver='auto', 
	# tol=0.0, iterated_power='auto', random_state=None).fit(trainx).explained_variance_ratio_
	# # print len(var)
	# trainx = pca_list(trainx,var)
	# testx = pca_list(testx, var)
	# print (len(trainx[0]))


	# print testx
	# print testy
	clf1 = model.random_forest_classifier()
	ins1 = clf1.fit(trainx, trainy)
	res11 = clf1.predict(trainx)
	res12 = clf1.predict(testx)

	clf2 = model.neural_network_classifier()
	ins2 = clf2.fit(trainx, trainy)
	res21 = clf2.predict(trainx)
	res22 = clf2.predict(testx)

	clf3 = model.knn_classifier()
	ins3 = clf3.fit(trainx, trainy)
	res31 = clf3.predict(trainx)
	res32 = clf3.predict(testx)

	clf4 = model.decision_tree_classifier()
	ins4 = clf4.fit(trainx, trainy)
	res41 = clf4.predict(trainx)
	res42 = clf4.predict(testx)

	clf5 = model.svm_classifier()
	ins5 = clf5.fit(trainx, trainy)
	res51 = clf5.predict(trainx)
	res52 = clf5.predict(testx)

	testx = []
	trainx = []
	for i in range(0,len(trainy)):
		trainx.append([res11[i], res21[i],res31[i],res41[i],res51[i]])
	for i in range(0, len(testy)):
		testx.append([res12[i], res22[i],res32[i],res42[i],res52[i]])


	clf6 = model.random_forest_classifier()
	ins6 = clf6.fit(trainx, trainy)
	res6 = clf6.predict(testx)


	print res6
	print ins6.score(testx,testy)

	# name_train = get_name(path_train)
	# name_test = get_name(path_test)























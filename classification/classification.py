#!/usr/local/bin/python
# coding:utf-8

import os
import model
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.decomposition import PCA

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

	for each in name_list:
		if each == ".DS_Store":
			continue
		data = readfile(os.path.join(path, each))
		data = data.split(",")
		# print data
		data.pop()
		data.pop(33)
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


	var = PCA(n_components=37, copy=True, 
	whiten=False, svd_solver='auto', 
	tol=0.0, iterated_power='auto', random_state=None).fit(trainx).explained_variance_ratio_
	# print len(var)
	trainx = pca_list(trainx,var)
	testx = pca_list(testx, var)
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
		testx.append([res12[i], res22[i],res32[i],res42[i],res52[i]])


	clf6 = model.random_forest_classifier()
	ins6 = clf6.fit(trainx, trainy)
	res6 = clf6.predict(testx)


	print res6
	print ins6.score(testx,testy)

	# name_train = get_name(path_train)
	# name_test = get_name(path_test)























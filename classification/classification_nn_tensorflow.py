#!/usr/local/bin/python
# coding:utf-8

import os
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from keras.callbacks import TensorBoard
from keras.layers import Dropout


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
			a = each.split("_")[0]
			y.append([label[a]])
	# print len(x)
	# print y
		# print data
def main(X_train, y_train, X_test, y_test):
	num_classes = 75
	# 		X_train[i][j] = int(X_train[i][j])
	# for i in range(0,len(X_test)):
	# 	for j in range(0,len(X_test[0])):
	# 		X_test[i][j] = int(X_test[i][j])
	X_train = np.array(X_train)
	X_test = np.array(X_test)
	# y_train = np.array(y_train)
	# y_test = np.array(y_test)
	y_train = np_utils.to_categorical(y_train,75)
	y_test = np_utils.to_categorical(y_test,75)
	# one hot encode outputs
	# y_train = np_utils.to_categorical(y_train,num_classes)
	# y_test = np_utils.to_categorical(y_test,num_classes)

	# design model
	model = Sequential()
	model.add(Dense(400, input_dim = 57, activation ='relu'))
	model.add(Dropout(0.2))
	model.add(Dense(300, input_dim = 400, activation ='relu'))
	model.add(Dropout(0.2))
	model.add(Dense(200, input_dim=300, activation='relu'))
	model.add(Dropout(0.2))
	model.add(Dense(200, input_dim=200, activation='relu'))
	model.add(Dropout(0.2))
	model.add(Dense(num_classes, activation = 'softmax'))
	# tensorboard = TensorBoard(log_dir='log', histogram_freq=0, write_graph=True, write_images=True)

	# print out summary of the model
	print(model.summary())
	tensorboard = TensorBoard(log_dir='log', histogram_freq=0, write_graph=True, write_images=True)
	# Compile model
	model.compile(loss ='categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
	
	# Fit the model
	his = model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 40, batch_size =100, verbose = 2, callbacks=[tensorboard])
	# Final evaluation of the model
	# print (max(his.history['val_acc']))
	# list_his.append(max(his.history['val_acc']))
	# loss.append(min(his.history['val_loss']))
	scores = model.evaluate(X_test, y_test, verbose=0)
	print("Baseline Error: %.2f%%" % (100-scores[1]*100))
	# print list_his
	# print loss



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
		a = name_list[i].split("_")[0]
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
	

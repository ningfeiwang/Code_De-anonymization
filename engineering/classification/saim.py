from __future__ import absolute_import
from __future__ import print_function
import numpy as np

import random
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Model,Sequential
from keras.layers import Input, Flatten, Dense, Dropout, Lambda, concatenate, Add
from keras.optimizers import RMSprop
from keras import backend as K
import os
from keras.callbacks import TensorBoard

CUDA_VISIBLE_DEVICES = '0'
os.environ["CUDA_VISIBLE_DEVICES"] = CUDA_VISIBLE_DEVICES

num_classes = 74
epochs = 10

# class Saim():
# 	def __kernel_initializer__(self. data_var):
# 		pass
# 	def define(self, input):

def compute_accuracy(y_true, y_pred):
    '''Compute classification accuracy with a fixed threshold on distances.
    '''
    pred = y_pred.ravel() < 0.5
    return np.mean(pred == y_true)


def accuracy(y_true, y_pred):
    '''Compute classification accuracy with a fixed threshold on distances.
    '''
    return K.mean(K.equal(y_true, K.cast(y_pred < 0.5, y_true.dtype)))


# the data, split betwee
def euclidean_distance(vects):
    x, y = vects
    return K.sqrt(K.maximum(K.sum(K.square(x - y), axis=1, keepdims=True), K.epsilon()))


def eucl_dist_output_shape(shapes):
    shape1, shape2 = shapes
    return (shape1[0], 1)


def contrastive_loss(y_true, y_pred):
    '''Contrastive loss from Hadsell-et-al.'06
    http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf
    '''
    margin = 1
    return K.mean(y_true * K.square(y_pred) +
                  (1 - y_true) * K.square(K.maximum(margin - y_pred, 0)))

def create_pairs(x, y):
    print(np.array(x).shape)
    pairs = []
    labels = []
    # nums = len(x)
    nums = 100
    for i in range(nums):
        for j in range(i, nums):
            
            # print (x)
            # print (np.array(ran1))
            z1, z2 = x[i], x[j]
            # print (z1)
            pairs +=[[z1, z2]]
            if y[i] == y[j]:
                labels += [0]
            else:
                labels += [1]

            # ran1 = []
            # ran2 = []
            # for k in range(0,90):
            #     ran1.append(random.random()*random.random()*1000.0)
            #     ran2.append(random.random()*random.random()*400.0)  
            # z1, z2 = np.array(ran1), np.array(ran2)
            # # print (z1)
            # pairs +=[[z1, z2]]
            # labels += [random.randint(0,1)]

    # # n = min([len(digit_indices[d]) for d in range(num_classes)]) - 1
    # for d in range(num_classes):
    #     print (len(digit_indices[d]))

    # n = -1
    # # print (n)
    # for d in range(num_classes):
    #     for i in range(n):
    #         z1, z2 = digit_indices[d][i], digit_indices[d][i + 1]
    #         pairs += [[x[z1], x[z2]]]
    #         inc = random.randrange(1, num_classes)
    #         dn = (d + inc) % num_classes
    #         z1, z2 = digit_indices[d][i], digit_indices[dn][i]
    #         pairs += [[x[z1], x[z2]]]
    #         labels += [1, 0]
    return np.array(pairs), np.array(labels)


def get_name(filename):
    name_list = os.listdir(filename)
    return name_list

def readfile(filename):
    with open(filename) as file:
        data = file.read()
    return data

class Saimese(object):
	def __init__(self):
		self.x_train, self.y_train, self.x_test, self.y_test = self.get_data()
		self.input_shape = self.x_train.shape[1:]
		self.model_l, self.model_r = self.base(self.input_shape)


	def get_data(self):
		label = {}
		name_list = get_name('./trainingfeature')
		p = 0
		for i in range(0,len(name_list)):
			if name_list[i] == ".DS_Store":
				continue
			a = name_list[i].split("_")[1]
			if a in label.keys():
				continue
			label[a] = p
			p += 1

		x_train = []
		y_train = []
		x_test = []
		y_test = []
		for path in ['./trainingfeature', './testingfeature']:
			name_list = get_name(path)
			data1 = readfile(os.path.join(path, name_list[0]))
			data1 = data1.split(",")
			# print data
			data1.pop()
			ori = len(data1)
			print (ori)
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
					if "train" in path:
						x_train.append(data)
						a = each.split("_")[1]
						y_train.append(label[a])
					else:
						x_test.append(data)
						a = each.split("_")[1]
						y_test.append(label[a])

		return np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)


	def base(self, input_shape):
		input = Input(shape=input_shape)
		# x = Flatten()(input)
		# print (input)
		# base_model = Saim().define(input)
		x = Dense(400, activation ='relu', name='l1')(input)
		x = Dropout(0.2,name='d1')(x)
		x = Dense(300, activation ='relu', name='l2')(x)
		x = Dropout(0.2,name='d2')(x)
		x = Dense(200, activation='relu', name='l3')(x)
		x = Dropout(0.2, name='d3')(x)
		x = Dense(200, activation='relu', name='l4')(x)
		x = Dropout(0.2, name='d4')(x)

		model_l = Model(inputs=input, outputs=x)
		model_r = Model(inputs=input, outputs=x)

		return model_l, model_r

	def saimese(self):
		self.model_l.load_weights('./weights/base_model.hdf5',by_name=True)
		self.model_r.load_weights('./weights/base_model.hdf5',by_name=True)

		input_a = Input(shape=self.input_shape)
		input_b = Input(shape=self.input_shape)

		# # because we re-use the same instance `base_network`,
		# # the weights of the network
		# # will be shared across the two branches
		processed_a = self.model_l(input_a)
		processed_b = self.model_r(input_b)
		# digit_indices = [np.where(y_train == i)[0] for i in range(num_classes)]
		# print(digit_indices)
		# tr_pairs, tr_y = create_pairs(x_train, digit_indices)
		tr_pairs, tr_y = create_pairs(self.x_train, self.y_train)
		# print (tr_pairs.shape)

		# digit_indices = [np.where(y_test == i)[0] for i in range(num_classes)]
		te_pairs, te_y = create_pairs(self.x_test, self.y_test)
		# print (te_pairs.shape)

		distance = Lambda(euclidean_distance,
		                  output_shape=eucl_dist_output_shape)
		# distance = Lambda(cosine_distance,
		#                   output_shape=cos_dist_output_shape)([processed_a, processed_b])

		# cos_distance = merge([input_a, input_b], mode='cos', dot_axes=1) # magic dot_axes works here!
		# cos_distance = Reshape((1,))(cos_distance)
		# cos_similarity = Lambda(lambda x: 1-x)(cos_distance)
		# input_a = Input(shape=(input_dim, 1))
		# input_b = Input(shape=(input_dim, 1))

		# cos_distance = merge([processed_a,processed_b], mode='cos', dot_axes=1) # magic dot_axes works here!
		# cos_distance = Reshape((1,))(cos_distance)
		# cos_similarity = Lambda(lambda x: 1-x)(cos_distance)

		# model = Model([input_a, input_b], [cos_similarity])

		model = Model([self.model_l.input, self.model_r.input], distance)

		# train
		print (model.summary())
		rms = RMSprop()
		tensorboard = TensorBoard(log_dir='log', histogram_freq=0,write_graph=True,write_images=True)
		model.compile(loss=contrastive_loss, optimizer=rms, metrics=[accuracy])
		model.fit([tr_pairs[:, 0], tr_pairs[:, 1]], tr_y,
		          batch_size=10,
		          validation_split=0.2,epochs=epochs,callbacks=[tensorboard])



		# print (model.summary())
		scores = model.evaluate([te_pairs[:, 0], te_pairs[:, 1]], te_y,verbose=0)
		# print (scores)
		# compute final accuracy on training and test sets
		y_pred = model.predict([tr_pairs[:, 0], tr_pairs[:, 1]])
		tr_acc = compute_accuracy(tr_y, y_pred)
		y_pred = model.predict([te_pairs[:, 0], te_pairs[:, 1]])
		print (y_pred)
		# a = y_pred[0]
		# # print (a)
		# for i in range(len(y_pred)):
		#     if a != y_pred[i]:
		#         print (a)
		te_acc = compute_accuracy(te_y, y_pred)

		print('* Accuracy on training set: %0.2f%%' % (100 * tr_acc))
		print('* Accuracy on test set: %0.2f%%' % (100 * te_acc))


if __name__ == '__main__':
	Saimese().saimese()


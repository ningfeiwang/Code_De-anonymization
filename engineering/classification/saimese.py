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
num_classes = 74
epochs = 10

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

def euclidean_distance(vects):
    x, y = vects
    return K.sqrt(K.maximum(K.sum(K.square(x - y), axis=1, keepdims=True), K.epsilon()))
    # return 1


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


# def create_pairs(x, digit_indices):
    '''Positive and negative pair creation.
    Alternates between positive and negative pairs.
    '''
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

def create_pairs_2(x1, x2, y1, y2):
    # print(np.array(xs).shape)
    pairs = []
    labels = []
    for i in range(len(x2)):
        for j in range(len(x1)):
            
            # print (x)
            # print (np.array(ran1))
            z1, z2 = x2[i], x1[j]
            # print (z1)
            pairs +=[[z1, z2]]
            if y2[i] == y1[j]:
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


def create_base_network(input_shape):
    '''Base network to be shared (eq. to feature extraction).
    # '''
    # print (input_shape)
    input = Input(shape=input_shape)
    # x = Flatten()(input)
    # print (input)
    x = Dense(400, activation ='relu',name='l1')(input)
    x = Dropout(0.2,name='d1')(x)
    x = Dense(300, activation ='relu',name='l2')(x)
    x = Dropout(0.2,name='d2')(x)
    x = Dense(200, activation='relu', name='l3')(x)
    x = Dropout(0.2,name='d3')(x)
    x = Dense(200, activation='relu', name='l4')(x)
    x = Dropout(0.2, name='d4')(x)

    # model.add(Dense(num_classes, activation = 'softmax'))
    # x = Dense(128, activation='relu')(x)
    # x = Dropout(0.1)(x)
    # x = Dense(128, activation='relu')(x)
    # x = Dropout(0.1)(x)
    # x = Dense(128, activation='relu')(x)
    return Model(input, x)


def compute_accuracy(y_true, y_pred):
    '''Compute classification accuracy with a fixed threshold on distances.
    '''
    pred = y_pred.ravel() < 0.5
    # print(pred)
    return np.mean(pred == y_true)


def accuracy(y_true, y_pred):
    '''Compute classification accuracy with a fixed threshold on distances.
    '''
    return K.mean(K.equal(y_true, K.cast(y_pred < 0.5, y_true.dtype)))


# the data, split between train and test sets
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train = x_train.astype('float32')
# x_test = x_test.astype('float32')
# x_train /= 255
# x_test /= 255
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
    # print (ori)
    for each in name_list:
        if each == ".DS_Store":
            continue
        data = readfile(os.path.join(path, each))
        data = data.split(",")
        # print data
        data.pop()
        # if len(data) >= 33:
        #   data.pop(33)
        l = len(data)
        # print (data)
        # print(np.array(data).shape)

        for k in range(0, len(data)):
            data[k] = float(data[k])
            # trainx.append()
        if l == ori:
            # print (data)
            x.append(data)
            a = each.split("_")[1]
            y.append([label[a]])




path_train = './trainingfeature'
path_test = './testingfeature'
x_test = []
y_test = []
x_train = []
y_train = []
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
# print(len(label.keys()))
# print (p)
# print len(label)
get_data(path_train, x_train, y_train, label)

get_data(path_test, x_test, y_test, label)
# print (y_test)


# num_classes = 74


x_train = np.array(x_train)
x_test = np.array(x_test)

# y_train = np_utils.to_categorical(y_train,74)
# y_test = np_utils.to_categorical(y_test,74)
y_train = np.array(y_train)
y_test = np.array(y_test)
# print (y_test)
# print (y_train)



input_shape = x_train.shape[1:]
# input_shape = (1090,)

# create training+test positive and negative pairs
digit_indices = [np.where(y_train == i)[0] for i in range(num_classes)]
# print(digit_indices)
# tr_pairs, tr_y = create_pairs(x_train, digit_indices)
tr_pairs, tr_y = create_pairs(x_train, y_train)
print (tr_pairs.shape)

digit_indices = [np.where(y_test == i)[0] for i in range(num_classes)]
# te_pairs, te_y = create_pairs_2(x_test, x_train, y_test, y_train)
te_pairs, te_y = create_pairs(x_test,  y_test)
print (te_pairs.shape)
te_y = np_utils.to_categorical(te_y,2)
tr_y = np_utils.to_categorical(tr_y,2)
# for i in range(len(te_))
# tr_y = np_utils.to_categorical(tr_y,2)
# te_y = np_utils.to_categorical(te_y,2)
# print (tr_pairs)
# print (te_y)

# network definition
base_network = create_base_network(input_shape)
base_network.load_weights("./weights/base_model.hdf5", by_name = True)

input_a = Input(shape=input_shape)
input_b = Input(shape=input_shape)

# because we re-use the same instance `base_network`,
# the weights of the network
# will be shared across the two branches
processed_a = base_network(input_a)
# processed_a.load_weights("./weights/base_model.hdf5", by_name = True)
processed_b = base_network(input_b)
# processed_b.load_weights("./weights/base_model.hdf5", by_name = True)

distance = Lambda(euclidean_distance,
                  output_shape=eucl_dist_output_shape)([processed_a, processed_b])
# print(distance)
# model = Model([input_a, input_b], distance)
# model = Model([input_a, input_b])
# model = Sequential()
# x = merge([processed_a, processed_b],mode='concat')
# x = Dense(3000, activation ='relu')(x)
# x = Dropout(0.2)(x)
# x = Dense(2000, activation='relu')(x)
# x = Dropout(0.2)(x)
# x = Dense(2000, activation='relu')(x)
# x = Dropout(0.2)(x)
# x = Dense(2, activation='softmax')(x)
# model = Model([input_a, input_b],x)
added = concatenate([processed_a, processed_b])  # equivalent to added = keras.layers.add([x1, x2])
print (processed_a.shape)
out = Dense(400,activation ='relu')(added)
out = Dropout(0.2)(out)
out = Dense(200,activation ='relu')(out)
out = Dropout(0.2)(out)
out = Dense(2,activation ='softmax')(out)
model = Model(inputs=[input_a, input_b], outputs=out)
model.summary()
# model.add(Add()([processed_a, processed_b]))
# model.add(400, activation ='relu')
# model.add(Dropout(0.2))
# model.add(200, activation ='relu')
# model.add(Dropout(0.2))
# model.add(Dense(2, activation='softmax'))

# train
rms = RMSprop()
tensorboard = TensorBoard(log_dir='log', histogram_freq=0,write_graph=True,write_images=True)
# model.compile(loss=contrastive_loss, optimizer=rms, metrics=[accuracy])
# model.fit([tr_pairs[:, 0], tr_pairs[:, 1]], tr_y,
#           batch_size=100,
#           validation_split=0.2,epochs=epochs,callbacks=[tensorboard])
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
model.fit([tr_pairs[:, 0], tr_pairs[:, 1]], tr_y, 
    validation_split=0.2, epochs=epochs, batch_size=32, verbose=2, callbacks=[tensorboard])
scores = model.evaluate([te_pairs[:, 0], te_pairs[:, 1]], te_y,verbose=0)
# print (scores)
# compute final accuracy on training and test sets
y_pred = model.predict([tr_pairs[:, 0], tr_pairs[:, 1]])
tr_acc = compute_accuracy(tr_y, y_pred)
# print (te_pairs[:,0])
# print(np.array([tr_pairs[:, 0], tr_pairs[:, 1]]).shape)
# print (x_train)
# print(len(x_train[1]))
# for i in range(len(x_test)):
#     min_pro = 0.0
#     index = 0
#     for j in range(len(x_train)):
#         # print(x_test)
#         # print(x_test[i,:])
#         # print()

#         z1, z2 = x_test[i], x_train[j]
#         # print(len(z1))
#         # print((np.array([np.array([z1]), np.array([z2])]).shape))
#         pre = model.predict([np.array([z1]), np.array([z2])])
#         if pre[0][0] > min_pro:
#             min_pro = pre[0][0]
#     print (min_pro)
        # print (pre)




y_pred = model.predict([te_pairs[:, 0], te_pairs[:, 1]])
# print (np.array(y_pred).shape)
print (model.predict([te_pairs[:, 0], te_pairs[:, 1]]))
te_acc = compute_accuracy(te_y, y_pred)

print('* Accuracy on training set: %0.2f%%' % (100 * tr_acc))
print('* Accuracy on test set: %0.2f%%' % (100 * te_acc))

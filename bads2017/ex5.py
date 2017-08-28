

import os
import numpy as np
np.random.seed(os.getpid()) #1337)  # for reproducibility

from keras.datasets import mnist, cifar10
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, Conv2DTranspose
from keras.layers.merge import Add, Concatenate

from keras.layers import Input, Dense, Activation, Flatten, Reshape, ActivityRegularization
from keras.layers.pooling import MaxPooling1D

from keras import regularizers
from keras import initializers
from keras.callbacks import Callback
from keras.layers import Convolution2D, MaxPooling2D, AveragePooling2D
from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.optimizers import SGD, Adam
from keras.utils import np_utils
import keras.backend as K
import numpy as np
import sys
import random


def create_res_basicblock( input_shape, k, reduce_first ):
    
    x = Input(shape=(input_shape))

    # shortcut path
    xx = x
    if reduce_first: # need to scale down
        xx = AveragePooling2D(pool_size=(2,2), padding='valid',
                              data_format='channels_first')(x)

    if k>input_shape[0]: # need to pad zero channels
        tmp = Conv2D(k-input_shape[0], (1,1), padding='same', use_bias=False,
                     data_format='channels_first', kernel_initializer='zero')(xx)
        tmp.trainable = False # no train, just zero
        xx = Concatenate(axis=1)([xx, tmp])
        
    # residual path
    residual = BatchNormalization(axis=1)(xx)
    residual = Activation('relu')(residual)
    residual = Conv2D(k, (3,3), padding='same', use_bias=False,
                      data_format='channels_first')(residual) 

    residual = BatchNormalization(axis=1)(residual)
    residual = Activation('relu')(residual)
    residual = Conv2D(k, (3,3), padding='same', use_bias=False,
                      data_format='channels_first')(residual)

    y = Add()([xx, residual]) 
    
    block = Model(inputs=[x], outputs=[y])
    return block



if __name__ == "__main__":

    # the data, shuffled and split between train and test sets
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    X_train /= 255
    X_test /= 255
    X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
    X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
    print('X_train shape:', X_train.shape)
    print(X_train.shape[0], 'train samples')
    print(X_test.shape[0], 'test samples')

    # convert class vectors to binary class matrices
    Y_train = np_utils.to_categorical(y_train, 10)
    Y_test = np_utils.to_categorical(y_test, 10)



    model = Sequential()
    model.add( Conv2D(10, (3,3), padding='same', use_bias=False, data_format='channels_first', input_shape=(1,28,28)) )
    model.add( create_res_basicblock((10,28,28), 10, False ) )
    model.add( create_res_basicblock((10,28,28), 20, True ) )
    model.add( create_res_basicblock((20,14,14), 40, True ) )
    model.add( BatchNormalization(axis=1) ) # BN
    model.add( Activation('relu') )
    model.add( Flatten() )
    model.add( Dense(10, activation='softmax') )
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    print model.summary()
    
    model.fit(X_train, Y_train, batch_size=64, epochs=5, verbose=1)
    score = model.evaluate(X_test, Y_test, verbose=0)
    print('Test score:', score[0])
    print('Test accuracy:', score[1])

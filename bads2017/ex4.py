
import os
import numpy as np
np.random.seed(os.getpid()) # 1337)  # for reproducibility  #

from keras.datasets import mnist
from keras.models import Sequential, Model
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from keras.layers import Flatten, Dense
from keras.utils import np_utils
from keras.layers.normalization import BatchNormalization
from keras.datasets import mnist, cifar10
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, Conv2DTranspose
from keras.layers.merge import Add, Concatenate
from keras.layers import Input, Dense, Activation, Flatten, Reshape, ActivityRegularization
from keras.layers.pooling import MaxPooling1D


def deepid_layerconv4( input_shape ):
    x = Input(shape=input_shape)
    y = Conv2D(80, (2,2),
               data_format='channels_first')(x)
    y = Flatten()(y)
    z = Flatten()(x)
    w = Concatenate()([y,z])
    r = Model(inputs=[x], outputs=[w])
    return r

deepid = Sequential()
deepid.add( Conv2D(20, (4,4), padding='valid', use_bias=True, activation='relu',
                   input_shape=(1,31,39), data_format='channels_first') )
deepid.add( MaxPooling2D(pool_size=(2,2), data_format='channels_first') )
deepid.add( Conv2D(40, (3,3), padding='valid', use_bias=True, activation='relu',
                   data_format='channels_first') )
deepid.add( MaxPooling2D(pool_size=(2,2), data_format='channels_first') )
deepid.add( Conv2D(60, (3,3), padding='valid', use_bias=True, activation='relu',
                   data_format='channels_first') )
deepid.add( MaxPooling2D(pool_size=(2,2), data_format='channels_first') )
deepid.add( deepid_layerconv4((60,2,3)) )
deepid.add( Dense(160, activation='relu') )
deepid.add( Dense(1000, activation='softmax') )
deepid.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


print deepid.summary()


deepid2 = Sequential()
deepid2.add( Conv2D(20, (4,4), padding='valid', use_bias=True, activation='relu',
                   input_shape=(1,31,39), data_format='channels_first') )
deepid2.add( MaxPooling2D(pool_size=(2,2), data_format='channels_first') )
deepid2.add( Conv2D(40, (3,3), padding='valid', use_bias=True, activation='relu',
                   data_format='channels_first') )
deepid2.add( MaxPooling2D(pool_size=(2,2), data_format='channels_first') )
deepid2.add( Conv2D(60, (3,3), padding='valid', use_bias=True, activation='relu',
                   data_format='channels_first') )
deepid2.add( MaxPooling2D(pool_size=(2,2), data_format='channels_first') )
deepid2.add( deepid_layerconv4((60,2,3)) )
deepid2.add( Dense(160, activation='relu') )
deepid2.add( Dense(10, activation='softmax') )

print deepid2.summary()

for i in range(len(deepid.layers)-1):
    deepid2.layers[i].set_weights( deepid.layers[i].get_weights() )
    deepid2.layers[i].trainable = False


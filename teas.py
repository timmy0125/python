import numpy as np
import panadas as pd
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.datasets import mnist
(x_train_image,y_train_label),(x_test_image, y_test_label) = mnist.load_data()

print ('x_train_image',x_train_image.shape)
print ('y_train_label',y_train_label.shape)

print('x_teat_image:', x_train_image.shape)
print('y_test_label:', y_test_label.shape)

def plot_image(image)
    fig=plt.gcf()
    fig.set_size_inches(2,2)
    plt.imshow(image, cmap='binary')
    plt.show

plot_image(x_train_image[0])

y_train_label[0]


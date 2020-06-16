import numpy as np
import panadas as pd
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.datasets import mnist
(x_train_image,y_train_label),(x_test_image, y_test_label) = mnist.load_data()
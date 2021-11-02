import os
import numpy as np
import keras
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import time
import tensorflow as tf
from keras import backend as K


#Prediction Function
def predict(model, file):

    img_width, img_height = 100,100
    x = load_img(file, target_size=(img_width,img_height))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = model.predict(x)
    result = array[0]
    #print(result)
    answer = np.argmax(result)
    return answer 

if __name__ == "__predict__":
    predict()
    
    

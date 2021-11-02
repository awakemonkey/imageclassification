from sklearn.datasets import load_files
from keras.models import load_model
from os.path import isfile, join
import streamlit as st
from os import listdir
from PIL import Image
import pandas as pd
import numpy as np
import keras
from keras import backend as K
import Testing
from Testing import predict


st.write("""
## Image Classification Prototype
""")

st.write("""
###### Peng Kong
""")

st.sidebar.info("This prototype  wiritten to help you understand how the trained Image Classification model help cusotmer to identify loosen items when self-checking in supermarket.")

showpred = 0
test_path = 'D:/ImageProject/TestImages/'
model_path = 'D:/ImageProject/model.h5'
model_weights_path = 'D:/ImageProject/weights.h5'

model = load_model(model_path)
model.load_weights(model_weights_path)

onlyfiles = [f for f in listdir(test_path) if isfile(join(test_path, f))]
st.title('Item Identification')
st.write("Pick an image from the left. You'll be able to view the image.")
    
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

st.sidebar.title("Predict New Images")
imageselect = st.sidebar.selectbox("Pick an image.", onlyfiles)
if  st.sidebar.button('Predict Item'):
    showpred = 1
    prediction = Testing.predict((model),test_path + imageselect)
    
st.write("")
image = Image.open(test_path + imageselect)
st.image(image, width = int, use_column_width=True)   

if showpred == 1:
    if prediction == 0:
        st.write("""
        # This is a Apple Gala!""")
    if prediction == 1:
        st.write("""
        # This is a Apple Green!""")
    if prediction == 2:
        st.write("""
        # This is a Apple Queen!""")
    if prediction == 3:
        st.write("""
        # This is a Apricot!""")
    if prediction == 4:
        st.write("""
        # This is a Avocado!""")
    if prediction == 5:
        st.write("""
        # This is a Avocado ripe!""")
    if prediction == 6:
        st.write("""
        # This is a Banana Lady Finger!""")
    if prediction == 7:
        st.write("""
        # This is a Eggplant!""")
    if prediction == 8:
        st.write("""
        # This is a Kiwi!""")
    if prediction == 9:
        st.write("""
        # This is a Onion Red!""")
    if prediction == 10:
        st.write("""
        # This is a Tomato!""")
import pandas as pd
import numpy as np
import streamlit as st
from os import listdir
from os.path import isfile, join
from PIL import Image
from keras.models import load_model
from keras import backend as K

st.write("""
## Image Classification Prototype
""")


st.write("""
#### Team Awake Monkey
###### Peng Kong
""")



st.sidebar.info("This prototype  wiritten to help you understand how the trained Image Classification model help cusotmer to identify loosen items when self-checking in supermarket.")



test_path = 'D:/ImageProject/TestImage/'
onlyfiles = [f for f in listdir(test_path) if isfile(join(test_path, f))]



    
st.title('Item Identification')
st.write("Pick an image from the left. You'll be able to view the image.")
st.write("When you're ready, submit a prediction on the left.")
    
st.sidebar.title("Predict New Images")
imageselect = st.sidebar.selectbox("Pick an image.", onlyfiles)
if st.sidebar.button('Predict Item'):
    showpred = 1
    prediction = Testing.predict((model),test_path + imageselect)
    
    
st.write("")
image = Image.open(test_path + imageselect)
st.image(image, caption="Let's predict the item!", use_column_width=True)    
    
    
        
    
    



<h1 align="center">Fruit and Vegetables Classification Model</h1>

<p align="left">This project is still on going and coding part is not finished yet. The code files just present a prototpye of Image Classification model, which trained by using tensorflow, keras and CNN algorithm. And the sp.py file shows how to present the model with an interactive UI and it is completed now.
The database used in this case is shorted by the original dataset from Fruit-360 on Kaggle, and the dataset maybe too large to run when training the model, so I only keep 11 items with more than 7,000 images for model training. 
If you want to use this code to train your own model, please remember to change the path of dataset, model, test_path and also the category name.</p>


This proposal still on going and here just the basic introduction of details. I choose to optimise self-checking process for customers who shopping in supermarket like Paknsave Or Countdown.




### Background: 
Since early 2020, Covid-19 spread all over the world and changed people’s lifestyle. When people shopping in supermarket, it is very often to see that customers ask help when they use self-checking machine to process check-out but can not find out the correct loosen items like fruits and vegetables to calculate the weight. There is no barcode or category tag attached on fruits and vegetables and some items are looks like very similar. It is very hard for customers to identify the correct items to measure the weight and staffs have to answer these help requests very often.

### Problem:
1. Help requests assigned to staffs are overwhelming and staffs are under pressure.
2. Increase the risk of infecting COVID-19 due to close contact (even keep 2 meters distance, but the virus still appeal on the surface of touched items, display screen of self-checking machine as example).

### Solution: 
To design a Machine Learning based add-on and installed on self-checking machine, to provide item recognition and classification function for customer when they want to find out the correct items and measure the weight in order to pay for the right items with right price calculation. 

### Application: 
Camera on self-checking machine will capture the loosen items customer picked, then based on Image recognition and Classification Model, the captured image will be processed and automatically be recognised as most possible category and specific item for customer to confirm.

### Language, library, algorithm in this case
- Python
- tensorflow
- keras
- sklearn
- pandas
- numpy
- **streamlit**

### Approach: 
Hardware layer: Camera installed on self-checking machine to capture items which customer picked and require to correctly identify and measure the weight.
Software layer: Use specific library/package (tensorflow and Keras)/algorithm (CNN) in Python to train and test Image Classification Model. 
Data layer: Data/Images may get from existed database (mostly downloaded from online) or manually take by staff on supermarket.

Training Image Classification Model: See Fruit_recognition_with_CNN_Original.ipynb


## In order to present how the model can be used to optimize self-checking process, an interactive UI is designed to combine the model with a simple UI, to give user a clear view how it will be operated in real world.
Prototype: see st.py




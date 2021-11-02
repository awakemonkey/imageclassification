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
- **CNN**

### Approach: 
Hardware layer: Camera installed on self-checking machine to capture items which customer picked and require to correctly identify and measure the weight.
Software layer: Use specific library/package (tensorflow and Keras)/algorithm (CNN) in Python to train and test Image Classification Model. 
Data layer: Data/Images may get from existed database (mostly downloaded from online) or manually take by staff on supermarket.

### Files in this model
- Fruit_recognition_with_CNN_Original.ipynb --- steps of how to use dataset to train a CNN model and save the models as h5 files for interactive UI)
- Test.py --- define a function which use saved model files to identify and predict the category of the input picture.
- st.py --- to design the interactive UI, contains UI components and also the functions behind of each elements

### How to deploy this model and interactive UI in your PC
1. Download all files and folders of this project.
2. Open Fruit_recognition_with_CNN_Original.ipynb by your code editor, such as jupyter notebook..
3. Change the path of 
```ruby
 train_dir = 'D:/Image Backup/Train'
 ```
 and
 ```ruby
test_dir = 'D:/Image Backup/Test'
```
to locate your onw train and test dataset.
4. Remember to print out the number of classes(categories) of dataset:
```ruby
# confirm the number of classes 
no_of_classes = len(np.unique(y_train))
no_of_classes
11
```
the number of classes in this model is the value of Dense in the following code
```ruby
model.add(Dense(11,activation = 'softmax'))
```
5. Models saved as h5 files and in the path you set as below, these two files are the key things for predict input images.
```ruby
model.save('model.h5')
model.save_weights('weights.h5')
```
6. Open st.py file in jupyter notebook or other options, change the path of following code to allocate the folder which contains images you want to predict and saved model files from **step 5**:
```ruby
test_path = 'D:/ImageProject/TestImages/'
model_path = 'D:/ImageProject/model.h5'
model_weights_path = 'D:/ImageProject/weights.h5'
```
7. Save st.py files, open terminal and allocate the folder contains st.py, input:
```ruby
streamlit run st.py
```
and you will see:
```ruby
![image](https://user-images.githubusercontent.com/39287382/139845553-76219f81-ae18-44aa-ad00-97c63422cb78.png)
```
9. Have fun and enjoy the **debugging**

## In order to present how the model can be used to optimize self-checking process, an interactive UI is designed to combine the model with a simple UI, to give user a clear view how it will be operated in real world.
Prototype: see st.py




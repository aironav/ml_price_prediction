import numpy as np
import streamlit as st
import pickle




def load_model(path_to_model):
    with open(path_to_model, 'rb') as f:
        return pickle.load(f)

st.sidebar.title('Insurance Price Predictor')


age = st.slider('Age', 0, 100,  key='slider1')

# Female = 0  Male = 1

s = st.selectbox('Sex', ('Male','Female'))
if s == 'Male':
    sex = 1
else:
    sex = 0


# Non Smoker = 0 Smoker = 1 

sm = st.selectbox('Do you Smoke', ('Smoker','Non Smoker'))
if sm == 'Smoker':
    smoker = 1
else:
    smoker = 0

bmi = st.number_input('Enter BMI:- ')

hd = st.number_input('Enter Number of Children:- ')

region = st.selectbox('Tick the Region you belong', ('Northeast is 0','Northwest is 1', 'Southeast is 2', 'Southwest is 3'))

if region == 'Northeast is 0':
    rg = 0
elif region == 'Northwest is 1':
    rg = 1
elif region == 'Southeast is 2':
    rg = 2
else:
    rg = 3




st.write('Age', + age)
st.write('Male(1) or Female(0):- ', + sex)
st.write('Smoker(1) or Non Smoker(0)', + smoker)
st.write('BMI', + bmi)
st.write('Children', + hd)
st.write('Region', rg )

bt = st.button('Show Insured Price')

if bt:
    model = load_model('../md_insure/random.pk')
    input_data = (age,sex,bmi,hd,smoker,region)
    input_data_as_numpy_array = np.array(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = random.predict(input_data_reshaped)
    print(prediction)
    print('The insurance cost is USD ', prediction[0])
    st.success(prediction)
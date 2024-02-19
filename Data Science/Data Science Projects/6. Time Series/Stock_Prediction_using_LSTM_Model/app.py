#Import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
#Load the model we already created to prevent running the epochs
from keras.models import load_model
import streamlit as st

#Define the starting and the ending point
start = '2010-01-01'
end = '2019-12-31'

st.title('Stock Trend Prediction')

#Take the input from the user
user_input = st.text_input('Enter stock Ticker', 'AAPL')
df = data.DataReader(user_input, 'stooq', start, end)

#Describing the Data
st.subheader('Data from 2010 - 2019')
st.write(df.describe())

#Visualizations
st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize = (12,6))
plt.plot(df.Close)
st.pyplot(fig)

#Moving Average for 100 and 200 days
st.subheader('Closing Price vs Time Chart with 100 & 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(ma100, 'r')
plt.plot(ma200, 'g')
plt.plot(df.Close, 'b')
st.pyplot(fig)

#Splitting the data into training and testing dataset
# 70% for training and 30% for testing
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])

# Scale the data between 0 and 1 through MinMax Scaler
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

#Fit the training data to our model and we convert our training data into an array
data_training_array = scaler.fit_transform(data_training)

#We don't need x_train and y_train because we are using the model that has already used these training datasets

#Load my model (which is already created in the jupyter file)
model = load_model('keras_model.h5')

#Testing Part
#For predicting the next 100 values we need values from the training data, so we append the training data into the testing data
past_100_days = data_training.tail(100)
final_df = past_100_days._append(data_testing, ignore_index=True)
#We scale the above data
input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100: i])
    y_test.append(input_data[i, 0])

x_test, y_test = np.array(x_test), np.array(y_test)

#Making Predictions
y_predicted = model.predict(x_test)

#We find the factor by how much they we were scaled down
scaler = scaler.scale_

#We convert them to the original value
scale_factor = 1/scaler[0]
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor

#Final Graph
#Plot the actual and the Predicted Price
st.subheader('Prediction Vs Actual')
fig2 = plt.figure(figsize=(12,6))
plt.plot(y_test, 'b', label = 'Original Price')
plt.plot(y_predicted, 'r', label = 'Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)
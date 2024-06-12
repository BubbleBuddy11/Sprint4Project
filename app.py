import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
from pathlib import Path

def preprocess_data(file_path):
    data = pd.read_csv(file_path)

    data['manufacturer'] = data['model'].apply(lambda x:x.split()[0])

    data['model_year'] = data.groupby('manufacturer')['model_year'].transform(lambda x: x.fillna(x.mode().iloc[0]))
    
    data['cylinders'] = data.groupby(['manufacturer', 'model'])['cylinders'].transform(lambda x: x.fillna(x.median()))

    data['odometer'] = data.groupby(['manufacturer', 'model_year'])['odometer'].transform(lambda x: x.fillna(x.median()))
    data['odometer'] = data['odometer'].fillna(data['odometer'].median())
    
    likely_4wd_types = ['SUV', 'pickup', 'truck', 'van', 'offroad', 'mini-van']
    data['is_4wd'] = data.apply(lambda row: 1.0 if pd.isna(row['is_4wd']) and row['type'] in likely_4wd_types else row['is_4wd'], axis=1)
    data['is_4wd'] = data['is_4wd'].fillna(0.0)
    data['is_4wd'] = data['is_4wd'].astype(bool)
    
    data['paint_color'] = data.groupby(['manufacturer'])['paint_color'].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 'Unknown'))
    data['paint_color'] = data['paint_color'].fillna(data['paint_color'].mode()[0])
    
    return data


data = preprocess_data(r'C:\Users\mercj\Sprint4Project\vehicles_us.csv')

st.header('Data Viewer')
st.dataframe(data)

st.header('Miles on Vehicle vs. Price by Manufacturer')
st.write(px.scatter(data, x='odometer', y='price', color='manufacturer').update_layout(xaxis_title='Odometer Reading', yaxis_title='Price'))

st.header('Distribution of Price')
st.write(px.histogram(data, x='price').update_layout(xaxis_title='Price', yaxis_title='Number of Vehicles'))

st.header('Price vs. Days Listed by Manufacturer')
st.write(px.scatter(data, x='price', y='days_listed', color='manufacturer').update_layout(xaxis_title='Price', yaxis_title='Number of Days Listed'))

st.header('Compare Price Distribution Between Vehicle Condition')
cond_list = sorted(data['condition'].unique())
cond_1 = st.selectbox('Select Vehicle Condition 1', cond_list, index=cond_list.index('excellent'))

cond_2 = st.selectbox('Select Vehicle Condition 2', cond_list, index=cond_list.index('salvage'))
mask_filter = (data['condition'] == cond_1) | (data['condition'] == cond_2)
data_filtered = data[mask_filter]
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None
st.write(px.histogram(data_filtered, x='price', nbins=30, color='condition', histnorm=histnorm, barmode='overlay'))
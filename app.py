import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front

## Please enter the parameters of the ride
'''

pd = st.date_input("Pickup date", datetime.date(2012, 10, 6))
pt = st.time_input('Pickup time', datetime.time(8, 45))
plon = st.number_input('Pickup longitude', 40., 42., 40.761)
plat = st.number_input('Pickup latitude', -75., -72., -73.98)
dlon = st.number_input('Dropoff longitude', 40., 42., 40.65)
dlat = st.number_input('Dropoff latitude', -75., -72., -73.88)
pcount = st.number_input('Passanger count', 1, 8, 1)

url = 'https://taxifare.lewagon.ai/predict'



if st.button('Submit'):
    params = {
        'pickup_datetime': datetime.datetime.combine(pd, pt).strftime('%Y-%m-%d %H:%M:%S'),
        'pickup_longitude': plon,
        'pickup_latitude': plat,
        'dropoff_longitude': dlon,
        'dropoff_latitude': dlat,
        'passenger_count': pcount
    }
    response = requests.get(url, params)

    fare = round(response.json().get('fare', 'I have fuckin no idea'), 2)

    st.markdown(f"### :tada: the fare is: ${fare}")

import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import datetime

st.set_page_config(
    page_title="Footix",
    page_icon=":soccer:",
    layout="wide",
    initial_sidebar_state="expanded",
    theme="green"
)

def get_fixtures(date):
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    querystring = {"date": date}
    headers = {
        "X-RapidAPI-Key": "267ed62edamshcb63a0412a87e53p112aa8jsn268e455bccf0",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)

    # extract information for each match and display it
    for match in data['response']:
        home_team = match['teams']['home']['name']
        away_team = match['teams']['away']['name']
        score = "{}-{}".format(match['goals']['home'], match['goals']['away'])
        st.write("{} vs. {}: {}".format(home_team, away_team, score))

# create a Streamlit app
st.title("Today's Football Fixtures")

# allow the user to input a date
date = st.date_input("Select a date", value=datetime.date.today())

# display the fixtures for the selected date
if st.button("Get Fixtures"):
    get_fixtures(str(date))

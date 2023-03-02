import requests
import json
import streamlit as st
import pandas as pd
import numpy as np
url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
querystring = {"date": "2023-03-02"}
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
    print("{} vs. {}: {}".format(home_team, away_team, score))

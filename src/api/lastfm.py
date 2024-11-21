# This file contains functions to interact with the API
import requests
import json

from database import tokens

root = "http://ws.audioscrobbler.com/2.0/"
api_key = tokens.LastFM()

def getRecentTracks(user, limit=50, page=1):
    url =  f"{root}?method=user.getrecenttracks&api_key={api_key}&format=json"
    url += f"&user={user}"
    url += f"&limit={limit}"
    url += f"&page={page}"
    data = requests.get(url).text
    return json.loads(data)

def getInfo(user):
    url =  f"{root}?method=user.getinfo&api_key={api_key}&format=json"
    url += f"&user={user}"
    data = requests.get(url).text
    return json.loads(data)

def getTopTracks(user, period="overall", limit=50, page=1):
    url =  f"{root}?method=user.gettoptracks&api_key={api_key}&format=json"
    url += f"&user={user}"
    url += f"&period={period}"
    url += f"&limit={limit}"
    url += f"&page={page}"
    data = requests.get(url).text
    return json.loads(data)
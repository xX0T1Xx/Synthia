import json

def Discord():
    return json.loads(open("data/tokens.json", "r").read())["Discord"]

def LastFM():
    return json.loads(open("data/tokens.json", "r").read())["LastFM"]
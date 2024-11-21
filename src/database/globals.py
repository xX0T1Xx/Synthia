# Contains variables used frequently in different places by the bot.
import json

def get_globals():
    file = open("data/globals.json", "r")
    data = json.loads(file.read())
    file.close()
    return data

def set_globals(data):
    file = open("data/globals.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()

def get_global(name):
    return get_globals()[name]

def set_global(name, value):
    globals = get_globals()
    globals[name] = value
    set_globals(globals)
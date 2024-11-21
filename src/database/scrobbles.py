from database import database
from utils import hash

# Format: [[username, uts, name, artist, album], ...]
def add_scrobbles(scrobbles):
    query = "INSERT OR IGNORE INTO scrobbles VALUES (?, ?, ?, ?, ?, ?)"
    params = []
    for scrobble in scrobbles:
        id = hash.md5(f"{scrobble[0].lower()}|{scrobble[1]}|{scrobble[2]}|{scrobble[3]}|{scrobble[4]}")
        params.append([id, scrobble[0].lower(), scrobble[1], scrobble[2], scrobble[3], scrobble[4]])
    database.run_many(query, params)

def get_scrobbles(username):
    query = "SELECT * FROM scrobbles WHERE username = ?"
    params = [username.lower()]
    return database.fetch(query, params)
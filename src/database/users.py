from database import database

def create_user(id):
    query = "INSERT OR IGNORE INTO users VALUES (?, ?)"
    params = [id, ""]
    database.run(query, params)

def set_username(id, username):
    query = "UPDATE users SET username = ? WHERE id = ?"
    params = [username, id]
    database.run(query, params)

def get_username(id):
    query = "SELECT * FROM users WHERE id = ?"
    params = [id]
    data = database.fetch(query, params)
    if len(data) == 0:
        return None
    else:
        return data[0][1]
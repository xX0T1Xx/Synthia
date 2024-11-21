import hashlib

def md5(string):
    return hashlib.md5(string.encode()).hexdigest()

def sha1(string):
    return hashlib.sha1(string.encode()).hexdigest()
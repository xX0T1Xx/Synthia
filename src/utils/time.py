from datetime import datetime

def timestamp(seconds):
    d = int(seconds / 86400);seconds %= 86400
    h = int(seconds / 3600);seconds %= 3600
    m = int(seconds / 60);seconds %= 60
    s = seconds
    string = ""
    if s: string = f"{s} second{'s' if s != 1 else ''} " + string
    if m: string = f"{m} minute{'s' if m != 1 else ''} " + string
    if h: string = f"{h} hour{'s' if h != 1 else ''} " + string
    if d: string = f"{d} day{'s' if d != 1 else ''} " + string
    return string[:-1]

def get_hour(unix_timestamp):
    hour = datetime.fromtimestamp(unix_timestamp).hour
    if hour == 0: return f"12 AM"
    elif hour < 12: return f"{hour} AM"
    elif hour == 12: return f"12 PM"
    else: return f"{hour-12} PM"

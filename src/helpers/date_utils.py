import datetime

def timestamp_as_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)
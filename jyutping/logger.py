import os

def log(message):
    if os.environ.get('JYUTPING_DEBUG'):
        print(message)

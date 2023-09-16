import json
from pymongo import MongoClient

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

url = config['mongourl']

def get_database():

    cluster = MongoClient(url)

    db = cluster['project1989']

    return db
import json
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Text, Optional
from events.logging import log, log_with_error

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

url = config['MONGO_URL']

def get_database() -> Database:
    cluster = MongoClient(url)
    db = cluster[config["DATABASE_NAME"]]
    return db

class CollectionNotFoundException(Exception):
    pass

def get_database_collection(collection_name: Text) -> Optional[Collection]:
    collection: Optional[Collection] = None

    try:
        if collection_name not in config["DATABASE_COLLECTIONS"]:
            raise CollectionNotFoundException()
        database = get_database()
        collection = database[collection_name]
    except Exception as error:
        log_with_error(f"Collection name '{collection_name}' is not found.", error)

    return collection
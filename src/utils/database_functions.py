from ..settings.app import todo_app
from abc import ABC, abstractmethod
from bson import ObjectId
from bson.errors import InvalidId
from pymongo import ReturnDocument
from datetime import datetime


class DatabaseFunctions(ABC):

    @abstractmethod
    def save(self, data): ...

    @abstractmethod
    def delete_by_id(self, record_id): ...

    @abstractmethod
    def filter(self, *args, **kwargs): ...

    @abstractmethod
    def fetch(self): ...

    @abstractmethod
    def update(self, data, record_id): ...


class MongoQueries(DatabaseFunctions):
    def __init__(self, collection_name):
        self.database = todo_app.db
        self.collection_name = collection_name

    def save(self, data):
        data.created_at = datetime.now()
        data.modified_at = datetime.now()
        data = data.dict(exclude_none=True)
        record_id = self.database.get_collection(self.collection_name).update_one({"name":data.get("name")}, {"$set":data}, upsert=True)
        return record_id

    def delete_by_id(self, record_id):
        delete_id=0
        try:
            delete_id=self.database.get_collection(self.collection_name).delete_one({"_id": ObjectId(record_id)}).deleted_count
        except (TypeError, InvalidId) as e:
            print("Invalid Object id")
        return delete_id

    def filter(self, *args, **kwargs):
        return self.database.get_collection(self.collection_name).find_one(kwargs) or {}

    def fetch(self):
        data = self.database.get_collection(self.collection_name).find({})
        return data

    def update(self, data, record_id):
        updated_data={}
        try:
            data.modified_at = datetime.now()
            updated_data = self.database.get_collection(self.collection_name).find_one_and_update(
                filter={"_id": ObjectId(record_id)},
                update={"$set": data.dict(
                    exclude_none=True)},
                return_document=ReturnDocument.AFTER)
        except (TypeError,InvalidId) as e:
            print("Invalid Object id")
        return updated_data

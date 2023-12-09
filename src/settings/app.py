import logging
import os
from .env_settings import config_env


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class AppMongo(metaclass=Singleton):
    logging.info("Database connection started")

    def __init__(self):
        env_detail = config_env.get(os.getenv('FN_ENV', 'default').lower())
        uri = getattr(env_detail, "DATABASE_HOST")
        self.db_name = getattr(env_detail, "DATABASE")
        from pymongo import MongoClient
        self.cx = MongoClient(uri)
        self.db = self.cx[self.db_name]
        logging.info("Database connection completed!")

    @classmethod
    def mongoDatabase(cls):
        return AppMongo().db


class App(metaclass=Singleton):

    def __init__(self):
        env_detail = config_env.get(os.getenv('Todo', 'default').lower())
        print(env_detail)
        for key in dir(env_detail):
            if key.isupper():
                setattr(self, key, getattr(env_detail, key))
        self.db = AppMongo.mongoDatabase()

    def get_db(self, db_name):
        return self.db.db[db_name]


todo_app = App()

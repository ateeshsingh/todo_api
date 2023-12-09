
class BaseConfig(object):
    DATABASE_HOST = "mongodb+srv://dev:atch20615008@mflix.34yoj.mongodb.net/?retryWrites=true&w=majority"
    DATABASE = "todo_database"
    JWT_SECRET="TOTO_SEcret"


config_env = dict(development=BaseConfig, default=BaseConfig)

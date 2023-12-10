from fastapi import APIRouter,HTTPException
from ..utils.database_functions import MongoQueries
from ..models.user_model import Users
from ..processor.authentication import UserCheck


class Login:
    mongo_queries = MongoQueries(collection_name="Users")


    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(path="/login", endpoint=self.user_login,
                                  methods=["GET"])
        self.router.add_api_route(path="/register-user", endpoint=self.register_users,
                                  methods=["POST"])

    def user_login(self, token: str):
        login = UserCheck(mongo_queries=self.mongo_queries)
        login_token=login.check_login(token=token)
        if login.response_code==0:
            raise HTTPException(status_code=400, detail={"response":login.response})
        return login_token

    def register_users(self, user: Users):
        user_register = UserCheck(mongo_queries=self.mongo_queries)
        return user_register.user_registration(user)




users = Login()

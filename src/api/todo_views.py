from fastapi import APIRouter, Header, HTTPException, Depends, status, Body
from ..models.todo_model import TodosCreate, TodosUpdate
from ..utils.database_functions import MongoQueries
from ..utils.jwt_encryption import JwtEncryption
from ..utils.examples import todos_request_body_example


class Todo:
    mongo_queries = MongoQueries(collection_name="Todos")

    def __init__(self):
        self.router = APIRouter(dependencies=[Depends(self.verify_auth)])
        self.router.add_api_route(path="/create-todos", endpoint=self.create_todo,
                                  methods=["POST"], status_code=status.HTTP_201_CREATED)
        self.router.add_api_route(path="/update-todos", endpoint=self.update_todo,
                                  methods=["PUT"], response_model=TodosUpdate)
        self.router.add_api_route(path="/delete-todos", endpoint=self.delete_todo,
                                  methods=["DELETE"])
        self.router.add_api_route(path="/get-todos", endpoint=self.get_todo,
                                  methods=["GET"])
        self.email = None

    def verify_auth(self, header=Header("Authorization")):
        encrypt = JwtEncryption()
        try:
            header_token = encrypt.decode_token(header)
            self.email = header_token.get("token")
        except Exception:
            raise HTTPException(status_code=401, detail={"response": "UnAuthorized"})

    async def create_todo(self, todo: TodosCreate = Body(..., example=todos_request_body_example)):
        todo.email = self.email
        response = self.mongo_queries.save(data=todo,name=todo.name)
        return todo

    async def update_todo(self, todo_id: str, todo: TodosUpdate = Body(..., example=todos_request_body_example)):
        todo.email = self.email
        response = self.mongo_queries.update(data=todo, record_id=todo_id)
        if not response:
            raise HTTPException(status_code=404, detail={"response": "Todo not found"})
        return response

    async def delete_todo(self, todo_id: str):
        response = self.mongo_queries.delete_by_id(record_id=todo_id)
        return response

    async def get_todo(self):
        response = self.mongo_queries.fetch(email=self.email)
        return [TodosUpdate(**item) for item in response]


todos = Todo()

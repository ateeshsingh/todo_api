from ..api.todo_views import todos
from ..api.login_view import users
from ..api.jwt_token_view import generate_token


class ApiRoutes:

    def __init__(self, app):
        app.include_router(generate_token.router, prefix="/api/v1", tags=["Token Generation For Login"])
        app.include_router(users.router, prefix="/api/v1", tags=["Login Users"])
        app.include_router(todos.router, prefix="/api/v1", tags=["Todos App"],dependencies=[])



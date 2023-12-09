from .urls import ApiRoutes
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def create_app():
    app = FastAPI(
        title="Todo Application",
        description="Documentation for Todo application Api's ",
        contact={
            "name": "Ateesh Chauhan",
            "email": "ateeshchauhan4023@gmail.com"
        }

    )
    ApiRoutes(app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


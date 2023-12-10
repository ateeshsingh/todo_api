import datetime

from main import app
import pytest
from httpx import AsyncClient

BASE_URL = "http://127.0.0.0.1:8000"


@pytest.mark.anyio
async def header_token():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        token = await ac.post(url="/api/v1/get-token", json={
            "email": "rk123@gmail.com",
            "password": "test"
        })
        response = await ac.get(
            url="/api/v1/login",
            params={"token": token.json()}
        )
    return response.json()


@pytest.mark.anyio
async def test_create_todo():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        deadline = "2023-12-10 09:55:24"
        response = await ac.post(url="/api/v1/create-todos",
                                 headers={"header": await header_token()},
                                 json={
                                     "name": "Playing Pubg and badminton",
                                     "description": "Play 24 hours pubg",
                                     "deadline": deadline

                                 }
                                 )
    assert response.status_code == 201
    return response


@pytest.mark.anyio
async def test_get_todo():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get(url="/api/v1/get-todos",
                                headers={"header": await header_token()}
                                )
    assert response.status_code == 200


@pytest.mark.anyio
async def test_update_todo():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.put(url="/api/v1/update-todos",
                                headers={"header": await header_token()},
                                params={"todo_id": "65753b4076d1d2f58c32a972"},
                                json={
                                    "name": "Playing Pubg and badminton",
                                    "description": "Play 24 hours pubg challenge",
                                    "deadline": "2023-12-10 09:55:24"
                                }
                                )
    assert response.status_code == 404


@pytest.mark.anyio
async def test_delete_todo():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.delete(url="/api/v1/delete-todos",
                                   headers={"header": await header_token()},
                                   params={"todo_id": "65753b4076d1d2f58c32a972"}
                                   )
    assert response.status_code == 200

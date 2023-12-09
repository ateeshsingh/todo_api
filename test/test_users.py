from main import app
import pytest
from httpx import AsyncClient

BASE_URL = "http://127.0.0.0.1:8000"


@pytest.mark.anyio
async def test_user_registration():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.post(url="/api/v1/register-user",
                                 json={
                                     "first_name": "Rahul",
                                     "last_name": "chauhan",
                                     "email": "rk123@gmail.com",
                                     "phone_no": "7505209121",
                                     "password": "test"
                                 }
                                 )
    assert response.status_code == 200


@pytest.mark.anyio
async def test_login():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        token = await ac.post(url="/api/v1/get-token", json={
            "email": "rk123@gmail.com",
            "password": "test"
        })
        response = await ac.get(
            url="/api/v1/login",
            params={"token": token.json()}
        )
    assert response.status_code == 200

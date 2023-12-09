from fastapi import APIRouter
from ..utils.jwt_encryption import JwtEncryption
from ..models.user_model import LoginModel


class GenerateToken:
    """
    Class Responsible For generating JWT Token which further passed as a header
    """
    jwt_token = JwtEncryption()

    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(path="/get-token", endpoint=self.get_token,
                                  methods=["POST"])

    def get_token(self, auth: LoginModel):
        return self.jwt_token.encode_token(data=auth.model_dump(exclude_none=True))


generate_token = GenerateToken()

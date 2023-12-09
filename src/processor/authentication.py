from ..utils.jwt_encryption import JwtEncryption
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHash, VerifyMismatchError


class UserCheck:

    def __init__(self, mongo_queries):
        self.mongo_queries = mongo_queries
        self.response=None
        self.response_code=0

    def check_login(self, token):
        jwt_enc = JwtEncryption()
        decode_data = jwt_enc.decode_token(token=token).get("token")
        user_record = self.mongo_queries.filter(email=decode_data.get("email"))
        if not user_record:
            self.response = "Invalid Email"
        try:
            if PasswordHasher().verify(user_record.get("password"), decode_data.get("password")):
                self.response = jwt_enc.encode_token(data=decode_data.get("email"), exp_time=30)
                self.response_code=200
        except (InvalidHash, VerifyMismatchError):
            self.response = "Invalid Password"
        return self.response

    def user_registration(self, user):
        if self.mongo_queries.filter(email=user.email):
            return
        password_hasher = PasswordHasher()
        user.password = password_hasher.hash(user.password)
        return self.mongo_queries.save(user)

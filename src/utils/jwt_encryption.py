import jwt
from datetime import datetime, timedelta
from ..settings.app import todo_app



class JwtEncryption:

    def encode_token(self, data,exp_time=30):
        token = jwt.encode({"token":data, "exp": datetime.utcnow() + timedelta(minutes=exp_time)},
                           todo_app.JWT_SECRET)
        return token

    def decode_token(self, token):
        decoded_data = {}
        try:
            decoded_data = jwt.decode(token, todo_app.JWT_SECRET, algorithms="HS256")
        except Exception as e:
            print(e)
        return decoded_data

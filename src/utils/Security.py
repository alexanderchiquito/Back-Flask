from decouple import config

import datetime
import jwt
import pytz
import traceback

# Logger
from src.utils.Logger import Logger


class Security():

    secret = config('JWT_KEY')
    tz = pytz.timezone("America/Lima")

    @classmethod
    def generate_token(cls, authenticated_user):
        try:
            payload = {
                'iat': datetime.datetime.now(tz=cls.tz),
                'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=10),
                'username': authenticated_user.USUARIO_ACCESO,
                'fullname': authenticated_user.USUARIO_ACCESO,
                'roles': ['Administrator', 'Editor']
            }
            return jwt.encode(payload, cls.secret, algorithm="HS256")
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    @classmethod
    def verify_token(cls, headers):
        try:
            if 'Authorization' in headers:
                authorization = headers['Authorization']
                print("Authorization header:", authorization)  # Depuración
                if authorization.startswith("Bearer "):
                    encoded_token = authorization.split(" ")[1]
                    print("Encoded token:", encoded_token)  # Depuración

                    if ((len(encoded_token) > 0) and (encoded_token.count('.') == 2)):  # Asegúrate de que el token sea válido
                        try:
                            payload = jwt.decode(encoded_token, cls.secret, algorithms=["HS256"])
                            roles = list(payload.get('roles', []))

                            if 'Administrator' in roles:
                                return True
                            return False
                        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                            return False
                return False
            return False
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return False
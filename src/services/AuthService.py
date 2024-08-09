import traceback
# Database
from src.database.db_mysql import get_connection
# Logger
from src.utils.Logger import Logger
# Models
from src.models.UserModel import User
#querys
from src.imports import *


class AuthService():

    @classmethod
    def login_user(cls, user):
        try:
            connection = get_connection()
            authenticated_user = None
            with connection.cursor() as cursor:
                cursor.execute(GET_AUTH_LOGIN, (user.USUARIO_ACCESO, user.CLAVE_ACCESO))
                # query = GET_AUTH_LOGIN
                # params = (user.USUARIO_ACCESO, user.CLAVE_ACCESO)
                # print("Executing query:", query)
                # print("With parameters:", params)
                # cursor.execute(query, params)

                row = cursor.fetchone()
                if row:
                    print("Query result:", row)
                    authenticated_user = User(row[0], row[1])
                else:
                    print("No matching user found")
            connection.close()
            return authenticated_user
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

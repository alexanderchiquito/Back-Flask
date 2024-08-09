import traceback
import pymysql
from src.database.db_mysql import get_connection
from src.utils.Logger import Logger
from src.models.StudentModel import Student
from src.sql.sqlQuerys import GET_STUDENT_BY_CARNET

class StudentService:

    @classmethod
    def get_students(cls, carnet):
        try:
            connection = get_connection()
            students = []
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(GET_STUDENT_BY_CARNET, (carnet,))
                resultset = cursor.fetchall()
                for row in resultset:
                    student = Student(row['CARNET'], row['NOMBRE'], row['PROGRAMA'])
                    students.append(student.to_json())
            connection.close()
            return students
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []

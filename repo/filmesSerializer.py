from settings import MYDB
import json
from datetime import datetime, time, timedelta
import decimal

class FilmeSerializer():
    @staticmethod
    def loadFilminhos():
        cursor = MYDB.cursor(dictionary=True)
        cursor.execute("select * from filminis.Filme")
        result = cursor.fetchall()

        for row in result:
            for key, value in row.items():
                if isinstance(value, (datetime, time, timedelta)):
                    row[key] = str(value)  
                elif isinstance(value, decimal.Decimal):
                    row[key] = float(value)

       
        return result
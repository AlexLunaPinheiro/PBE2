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
        cursor.close()            

        return result


    def criarFiliminho(filme):
        cursor = MYDB.cursor(dictionary=True)

        filmes = """SELECT titulo FROM filminis.filme"""
        cursor.execute(filmes)
        result = cursor.fetchall()

        cursor.close()

        jaEstaCadastrado = False

        for filminho in result:
            if filme["nome"] == filminho["titulo"]:
                jaEstaCadastrado = True

        if jaEstaCadastrado == False:
            cursor = MYDB.cursor(dictionary=True)
            query = """
                    INSERT INTO filminis.filme (titulo, orcamento, tempo_duracao, ano, poster)
                    VALUES (%s, %s, %s, %s, %s)
                """
                
            values = (
                filme["nome"],
                filme["orcamento"],
                filme["duracao"],
                filme["ano"],
                filme["poster"]
            )

            cursor.execute(query, values)
            MYDB.commit()
            return 201
        else:
            return 409
        
    def atualizar(pk: int):
        pass

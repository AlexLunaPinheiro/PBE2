import os
import json


def apagarCard(id):
     if os.path.exists("dados.json"):
        try:
            with open("dados.json", encoding="utf-8") as f:
                data = json.load(f)  
                if data != []: 
                    data.remove(data[id])
                
            with open("dados.json", "w", encoding="utf-8") as lista:
                    json.dump(data,lista,indent=4,ensure_ascii=False)

        except ( json.JSONDecodeError):
                data = []
                print("errado")
            

apagarCard(1)
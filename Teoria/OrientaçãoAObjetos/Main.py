import time
from Tamagoshi import Tamagoshi
tempo = 0


def jogo():
    print()

def main():
    while True:
        tempo+=1
        time.sleep(1)
        decisao = int(input("Digite 1 para jogar\nDigite 2 para sair"))
        if decisao == 1:
            jogo()

        elif decisao == 2: 
            break



    
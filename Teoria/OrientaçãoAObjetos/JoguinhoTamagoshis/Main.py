import time
import os
from Tamagoshis.Breeds import Pirata, Marinheiro, Revolucionario

def limpar_tela():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

def exibir_status(personagem):
    limpar_tela()
    print("="*30)
    print(f"  Nome: {personagem.nome} ({type(personagem).__name__})")
    print(f"  Idade: {personagem.idade:.1f} dias")
    print(f"  Saúde: {personagem.saude:.1f} / 100")
    print(f"  Fome: {personagem.fome:.1f} / 100")
    print(f"  Tédio: {personagem.tedio:.1f} / 100")
    print(f"  Força: {personagem.forca:.0f}") 
    print(f"  Humor (quanto maior, pior): {personagem.getHumor():.1f}")
    print("="*30)

def criar_inimigo(nivel):
    forca_base = 35
    forca_inimigo = forca_base + (nivel * 15)
    nomes = ["Bandido Fraco", "Pirata Rival", "Agente da CP5", "Capitão da Marinha Local", "Caçador de Recompensas"]
    nome_inimigo = nomes[(nivel - 1) % len(nomes)]
    return {"nome": nome_inimigo, "forca": forca_inimigo}

def jogo():
    limpar_tela()
    nome = input("Qual o nome do seu personagem? ")
    
    raca = ""
    while raca not in ['1', '2', '3']:
        raca = input("Escolha a raça:\n1. Pirata\n2. Marinheiro\n3. Revolucionário\n> ")
    
    forca_inicial = 50
    if raca == '1':
        personagem = Pirata(nome, 15, 100, 0, 10, forca_inicial)
    elif raca == '2':
        personagem = Marinheiro(nome, 10, 110, 0, 15, forca_inicial)
    else:
        personagem = Revolucionario(nome, 20, 90, 0, 20, forca_inicial)

    nivel_inimigo = 1 

    while personagem.saude > 0:
        exibir_status(personagem)
        
        print("Ações disponíveis:")
        print(f"1. Alimentar (com {personagem.forca}de poder)")
        print("2. Brincar (com 50 de poder)")
        
        if type(personagem) == Pirata:
            print("3. Caçar Tesouro")
            print("4. Beber Rum")
        elif type(personagem) == Marinheiro:
            print("3. Treinar Disciplina")
            print("4. Patrulhar a Costa")
        elif type(personagem) == Revolucionario:
            print("3. Discursar para o Povo")
            print("4. Planejar a Revolução")
        
        print("\n5. BATALHAR")
        print("0. Esperar (passar o tempo)")
        
        acao = input("> ")

        if acao == '1': personagem.alimentar(50)
        elif acao == '2': personagem.brincar(50)
        elif acao == '0': pass
        elif type(personagem) == Pirata and acao == '3': personagem.cacar_poneglyph()
        elif type(personagem) == Pirata and acao == '4': personagem.beber_rum()
        elif type(personagem) == Marinheiro and acao == '3': personagem.treinar_disciplina()
        elif type(personagem) == Marinheiro and acao == '4': personagem.patrulhar_a_costa()
        elif type(personagem) == Revolucionario and acao == '3': personagem.discursar_para_o_povo()
        elif type(personagem) == Revolucionario and acao == '4': personagem.planejar_a_revolucao()
        
        elif acao == '5': 
            inimigo_atual = criar_inimigo(nivel_inimigo)
            resultado = personagem.batalhar(inimigo_atual)
            
            if "vitoria" in resultado:
                nivel_inimigo += 1 
                print(f"Sua força aumentou para {personagem.forca:.0f}! O próximo oponente será mais forte.")
            
            time.sleep(4) 
            continue 

        else:
            print("Ação inválida!")

        print("\nO tempo passa...")
        time.sleep(1.5)
        personagem.tempoPassado()

    exibir_status(personagem)
    print(f"\nFIM DE JOGO! A jornada de {personagem.nome} chegou ao fim.")

def main():
    while True:
        limpar_tela()
        decisao = input("Digite 1 para jogar\nDigite 2 para sair\n> ")
        if decisao == '1':
            jogo()
            input("\nPressione Enter para voltar ao menu...")
        elif decisao == '2':
            print("Até a próxima!")
            break

if __name__ == "__main__":
    main()
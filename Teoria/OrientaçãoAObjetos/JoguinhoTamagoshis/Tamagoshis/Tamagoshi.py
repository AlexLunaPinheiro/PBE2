class Tamagoshi:
    def __init__(self, nome, fome, saude, idade, tedio, forca):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = tedio
        self.forca = forca

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100)

    def brincar(self, quantidade):
        self.tedio -= self.tedio * (quantidade/100)

    def getHumor(self):
        return ((self.fome + self.tedio)/2)
    
    def vida(self):
        if ((self.fome > 50 and self.fome <= 60)) or (self.tedio > 50 and self.tedio <= 60):
            self.saude -= 10
        elif ((self.fome > 60 and self.fome <= 80)) or (self.tedio > 60 and self.tedio <= 80):
            self.saude -= 30
        elif ((self.fome > 80 and self.fome <= 90)) or (self.tedio > 80 and self.tedio <= 90):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            print(f"{self.nome} está quase em frangalhos!")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print(f"{self.nome} vai jogar pelo gigante da colina em 2025.")

    def tempoPassado(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5

    def batalhar(self, oponente):
        print(f"--- BATALHA! ---\n{self.nome} (Força: {self.forca:.0f}) VS {oponente['nome']} (Força: {oponente['forca']})\n")

        if self.forca > oponente['forca'] * 1.3:
            print(f"Você usou o Haki do Rei! {oponente['nome']} foi obliterado!")
            self.forca *= 1.10 
            return "vitoria_haki"
        
        elif self.forca > oponente['forca']:
            print("Você venceu a batalha!")
            self.forca *= 1.10
            return "vitoria"

        elif self.forca == oponente['forca']:
            print("Empate! Seus caminhos irão se cruzar no futuro...")
            self.saude /= 2
            self.forca *= 1.5
            return "empate"

        else:
            print(f"A vida na Grand Line não é nada fácil, o golpe de {oponente['nome']} foi fatal.")
            self.saude = 0
            return "derrota"
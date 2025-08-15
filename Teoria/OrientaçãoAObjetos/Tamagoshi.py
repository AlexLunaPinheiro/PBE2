class Tamagoshi:
    def __init__(self, nome , fome , saude, idade, tedio, salario):
        self.nome = nome
        self.fome = 0 
        self.saude = 100
        self.idade = 0
        self.tedio = 0

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
            print("me ve um prato de comida ai pra mim")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print(f"{self.nome} está morto.")

    def tempoPassado(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5
        
        


    

    


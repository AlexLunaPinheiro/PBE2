from Tamagoshi import Tamagoshi

class Pirata(Tamagoshi):
    def __init__(self, nome , fome , saude, idade, tedio, salario):
        super().__init__(nome, fome, saude, idade, tedio , salario)

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100)

    

class Marinheiro(Tamagoshi):
    def __init__(self, nome , fome , saude, idade, tedio, salario):
        super().__init__(nome, fome, saude, idade, tedio , salario)

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 150)


class Revolucionario(Tamagoshi):
    def __init__(self, nome , fome , saude, idade, tedio, salario):
        super().__init__(nome, fome, saude, idade, tedio , salario)

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 200)


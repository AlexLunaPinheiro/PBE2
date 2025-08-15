class Veiculo:
    def __init__(self, cor, marca, qtdPortas: int,anoFabricacao: int):
        self.cor = cor
        self.marca = marca
        self.anoFabricacao = anoFabricacao
        self.qtdPortas = qtdPortas

    def andar(self):
        if self.__class__.__name__ == "Carro" or self.__class__.__name__ == "Caminhao":
            return f"o {self.__class__.__name__} {self.marca} está andando!"
        
        else:
            return f"a {self.__class__.__name__} {self.marca} está andando!"
        
    def imprimir(self):
        veiculo = self.__dict__
        for key, value in veiculo.items():
            print(f"{key}: {value}")

        
class Carro(Veiculo):
    def __init__(self, cor, marca, qtdPortas, anoFabricacao, qtdEixos, carroceria):
        super().__init__(cor, marca, anoFabricacao, qtdPortas)
        self.qtdEixos = qtdEixos
        self.carrocerida = carroceria

        
class Moto(Veiculo):
    def __init__(self, cor, marca, qtdPortas, anoFabricacao, cilindradas: int):
        super().__init__(cor, marca, anoFabricacao, qtdPortas)
        self.cilindradas = cilindradas

    
class Caminhao(Veiculo):
    def __init__(self, cor, marca, qtdPortas,  anoFabricacao, carga: float):
        super().__init__(cor, marca, anoFabricacao, qtdPortas)
        self.carga = carga

    
    def peso(self):
        return f"O caminhão aguenta {self.carga}KGs de peso"
        
    
carro1 = Carro("Azul", "BMW", 1984, 4, 4, "Sedan")
moto1 = Moto("Preta", "Suzuki", 2012, 0, 150)
caminhao1 = Caminhao("branca", "Scania", 2020, 2, 200)

carro1.imprimir()
print(carro1.andar())

moto1.imprimir()
print(moto1.andar())

caminhao1.imprimir()
print(caminhao1.andar())


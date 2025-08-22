from Tamagoshis.Tamagoshi import Tamagoshi

class Pirata(Tamagoshi):
    def __init__(self, nome, fome, saude, idade, tedio, forca):
        super().__init__(nome, fome, saude, idade, tedio, forca)

    def alimentar(self, quantidade):
        print(f"{self.nome}, deu uma grande festança!")
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 80)
            if self.fome < 0: self.fome = 0

    def batalhar(self, oponente):
        print("Boas batalhas edificam a alma de um verdadeiro pirata!")
        resultado = super().batalhar(oponente) 
        if "vitoria" in resultado: 
            self.tedio -= 40
            if self.tedio < 0: self.tedio = 0
        return resultado

    def cacar_poneglyph(self):
        print(f"{self.nome} caçou um poneglyph e teve várias aventuras")
        self.tedio -= 25
        if self.tedio < 0: self.tedio = 0

    def beber_rum(self):
        print(f"{self.nome} encheu a cara de rum! Mas os rins do coitado...")
        self.tedio -= 15
        self.saude -= 5
        if self.tedio < 0: self.tedio = 0

class Marinheiro(Tamagoshi):
    def __init__(self, nome, fome, saude, idade, tedio, forca):
        super().__init__(nome, fome, saude, idade, tedio, forca)
    
    def alimentar(self, quantidade):
        print(f"{self.nome}, como um bom e disciplinado funcionário da marinha, come regradamente sua refeição.")
        super().alimentar(quantidade)

    def batalhar(self, oponente):
        print("Para um marinheiro, o combate é um dever necessário, mas pode ser doloroso e acabar machucando outras pessoas.")
        self.saude -= 10 
        resultado = super().batalhar(oponente)
        return resultado

    def treinar_disciplina(self):
        print(f"{self.nome} fez um treinamento rigoroso. É tedioso, mas fortalece!")
        self.tedio += 10
        self.saude += 5
        if self.saude > 100: self.saude = 100

    def patrulhar_a_costa(self):
        print(f"{self.nome} patrulhou a costa. Mal pode esperar para dormir após um longo dia de trabalho !")
        self.tedio -= 10
        self.fome += 5
        if self.tedio < 0: self.tedio = 0

class Revolucionario(Tamagoshi):
    def __init__(self, nome, fome, saude, idade, tedio, forca):
        super().__init__(nome, fome, saude, idade, tedio, forca)

    def alimentar(self, quantidade):
        print(f"{self.nome}, o Revolucionário, precisa racionar o pouco que tem.")
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 120)
            if self.fome < 0: self.fome = 0
    
    def batalhar(self, oponente):
        print("Um revolucionário luta não por prazer nem muito menos pelo governo, mas pela causa. É indiferente.")
        resultado = super().batalhar(oponente)
        return resultado # Nenhum efeito de humor ou saúde

    def discursar_para_o_povo(self):
        print(f"{self.nome} fez um discurso inflamado pela liberdade! Que emocionante!")
        self.tedio -= 20
        self.fome += 5
        if self.tedio < 0: self.tedio = 0
    
    def planejar_a_revolucao(self):
        print(f"{self.nome} passou horas planejando. Cansativo, mas quem saiba agora IMU sama vá cair!!!")
        self.tedio += 15
        self.saude += 5
        if self.saude > 100: self.saude = 100
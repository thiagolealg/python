class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor
        print("cor trocada com sucesso")

    def mostraCor(self):
        return print(f"a cor da bola é {self.cor}")

bola1 = Bola("azul", "50", "pedra")
print(bola1.circunferencia)
print(bola1.cor)
bola1.trocaCor("amarela")
bola1.mostraCor()



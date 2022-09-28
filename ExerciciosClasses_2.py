#Quadrado: Crie uma classe que modele um quadrado:

#    Atributos: Tamanho do lado
#    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, tamanholado):
        self.tamanholado = tamanholado

    def alteratamanho(self, tamanholado):
        self.tamanholado = tamanholado
        print('tamanho alterado com sucesso')

    def tamanhoLado(self):
        return print(f"o comprimento do lado é {self.tamanholado}")

    def calculaArea(self):
        area = self.tamanholado*self.tamanholado
        print(f'a área total do quadrado é de {area}')


quadrado1 = Quadrado(25)
quadrado1.alteratamanho(50)
quadrado1.tamanhoLado()
quadrado1.calculaArea()
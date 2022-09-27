
def escolha_de_numero():
    a = int(input("escolha um número de 1 a 10: "))
    lista = list(range(11))
    while a not in lista:
        print("número inválido, escolha outro.")
        a= int(input("escolha um número de 1 a 10: "))

    print("número válido")

escolha_de_numero()





# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

print("Esse programa armazena 20 números e os separa entre ímpares e pares.")
print("--------------------------------------------------------------------\n")
lista_numeros = []
lista_impares = []
lista_pares = []
numeros = 0

while  len(lista_numeros) < 20:
    numero = input("escolha 20 números. A cada número digite ENTER. \n"
                   "Digite o número aqui: ")
    while not numero.isdigit():
        print("Escolha um valor numérico!!\n")
        numero = input("escolha 20 números. A cada número digite ENTER.")
    lista_numeros.append(numero)
    if int(numero) % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

    numeros = numeros + 1
    print("--------------------------- \n")
    print(f'você escolheu {numeros} numero(s).')

print(lista_numeros)
print(lista_impares)
print(lista_pares)
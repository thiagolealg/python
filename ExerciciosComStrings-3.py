#3- Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

print("----------------------------------------------------------------------\n")
print("Esse programa imprime o nome informado em maiúsculo na vertical.")
print("----------------------------------------------------------------------\n")

nome = input("digite seu nome: \n"
             ">> ")
nome = str(nome)
nome = nome.upper()
lista = list(nome)


for i in lista:
    print(i)
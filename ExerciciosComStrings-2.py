#2- Nome ao contrário em maiúsculas.
# Faça um programa que permita
# #ao usuário digitar o seu nome
# e em seguida mostre o nome do usuário de trás
# para frente utilizando somente letras maiúsculas.
# Dica: lembre−se que ao informar o nome o usuário
# pode digitar letras maiúsculas ou minúsculas.
#https://wiki.python.org.br/ExerciciosComStrings

print("----------------------------------------------------------------------\n")
print("Esse programa imprime o nome informado em maiúsculo de forma invertida")
print("----------------------------------------------------------------------\n")

nome = input("digite seu nome: \n"
             ">> ")
nome = str(nome)
nome = nome.upper()
print(list(nome))
new_nome =nome[::-1]
print(list(new_nome))
print(new_nome)
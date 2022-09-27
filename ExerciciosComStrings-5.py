#5- Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

print("----------------4------------------------------------------------------\n")
print("Esse programa imprime o nome informado em maiúsculo em escada invertida.")
print("----------------------------------------------------------------------\n")

nome = input("digite seu nome: \n"
             ">> ")
nome = str(nome)
nome = nome.upper()
lista = list(nome)
x = (len(lista))

for i in range(0,x):
    if i < x:
        print(nome[0:x-i])

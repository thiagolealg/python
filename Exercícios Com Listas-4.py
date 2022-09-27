#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
lista_final = []
lista = ['1', '2', 'c', 'd', 'e', 'f', 'a', 't', 'e', 'i']
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g' ',h', 'j', ' k', 'l', 'm', 'n', 'p', 'q' 'r', 's', 't', 'v', 'x', 'w', 'y', 'z']
for i in lista:
    if i in consoantes:
        lista_final.append(i)

print(lista_final)

print(f'São {len(lista_final)} caracteres')
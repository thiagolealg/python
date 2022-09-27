#Tamanho de strings.
# Faça um programa que leia 2 strings
# e informe o conteúdo delas seguido
# do seu comprimento.
# Informe também se as duas strings
# possuem o mesmo comprimento e são
# iguais ou diferentes no conteúdo.
print("-----------------------------------------------")
print("Esse programa permite comparar strings \n"
      "e calcula a quantidade de caracteres.")
print("-----------------------------------------------")
st1 = input("Informe o conteúdo: ")
st2 = input("Digite outro conteúdo para comparação: ")

if st1 == st2:
    cont = "igual"
else:
    cont = "diferente"
st1_c = len(st1)
st2_c = len(st2)
if st1_c == st2_c:
    carac = "iguais"
else:
    carac = "diferentes"

print(f'{st1}: {st1_c} caracteres')
print(f'{st2}: {st2_c} caracteres')

print(f'As duas strings são de tamanhos {carac}.')
print(f'As duas strings possuem conteúdo {cont}.')

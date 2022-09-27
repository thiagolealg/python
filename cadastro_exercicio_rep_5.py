## população A corresponde a 80000 habitantes com crescimento anual de 3%

## população B corresponde a 200000 habitantes com crescimento de 1.5%

## Quantos anos são necessários para a população A ser maior que a população B?
print("-------------------------------------------------")
print("Programa de simulação de crescimento populacional")
print("-------------------------------------------------")
print("-------------------------------------------------\n")
print("Defina a porcentagem da população de A e da população B.")
print("-------------------------------------------------\n")

pop_a = input("Defina o percentual de crescimento para a população A.\n"
					"digite o percentiual aqui: \n")

while not pop_a.isdigit():
	print("Escolha um valor numérico!!\n")
	pop_a = input("Defina o percentual de crescimento para a população A.\n"
						"digite o percentual aqui: ")

pop_b = input("Defina o percentual de crescimento para a população B.\n"
					"digite o percentiual aqui: \n")

while not pop_a.isdigit():
	print("Escolha um valor numérico!!\n")
	pop_a = input("Defina o percentual de crescimento para a população A.\n"
						"digite o percentual aqui: ")


pop_a = float(pop_a)
pop_b = float(pop_b)
a = 80000
b = 200000
x= 0
while a <= b:
	a = a*(1 + pop_a/100)
	b = b*(1 + pop_b/100)
	x = x+1

print(f' Em {x} anos a população de A será maior que a população de B.')



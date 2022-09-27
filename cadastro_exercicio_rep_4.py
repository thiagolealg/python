## população A corresponde a 80000 habitantes com crescimento anual de 3%

## população B corresponde a 200000 habitantes com crescimento de 1.5%

## Quantos anos são necessários para a população A ser maior que a população B?

a = 80000
b = 200000
x= 0
while a <= b:
	a = a*1.03
	b = b*1.015
	x = x+1

print(f' Em {x} anos a população de A será maior que a população de B.')



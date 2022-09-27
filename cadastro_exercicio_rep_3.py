print("Realize seu cadastro")
print("-----------------------")
#nome maior que 3 caracteres;

nome = str(input("digite seu nome: "))
while(len(nome)<=3):
	print("Favor digite mais que 3 caracteres")
	nome = str(input("digite seu nome: "))
print("-----------------------")

#Idade: entre 0 e 150;


idade = int(input("digite sua idade: "))
while ( idade > 150 or idade < 0 ):
	print("Favor escolha uma idade entre 0 a 150")
	idade = int(input("digite sua idade: "))
print("-----------------------")

#Salário: maior que zero;

salario = float(input("digite seu salario: "))
while ( salario < 0 ):
	print("Informe um valor acima de 0.")
	salario = float(input("digite seu salario: "))
print("-----------------------")

#Sexo: 'f' ou 'm';

sexo = str(input("digite seu sexo com a inicial (f ou m): "))
while sexo !="f" and sexo!="m" :
	print("sexo não válido, favor tente novamente. ")
	sexo = str(input("digite seu sexo com a inicial (f ou m): "))
print("-----------------------")

#Estado Civil: 's', 'c', 'v', 'd';

lista_est = ['s','c','v','d']
estado_civil = str(input("Informe seu estado civil, use apenas a letra incial.\n"
						 "solteiro(a) - s\n"
						 "casado(a)  - c\n"
						 "viúvo(a) - v\n"
						 "divorciado(a) - d\n"
						 "informe aqui: "))
while estado_civil not in lista_est:
	estado_civil = str(input("Valor inválido. Informe seu estado civil novamente: "))
print("----------------------------------------------------------------\n")
print("------------------------------")
print("Cadastro efetuado com sucesso.")
print("------------------------------")


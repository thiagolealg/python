# 4- Faça um programa, com uma função
# que necessite de três argumentos,
# e que forneça a soma desses três argumentos.
def soma(a,b,c):
    print (int(a)+int(b)+int(c))


soma(1,2,3)

# 5- Faça um programa, com uma função
# que necessite de um argumento.
# A função retorna o valor de caractere ‘P’
# , se seu argumento for positivo, e ‘N’
# , se seu argumento for zero ou negativo.

def positivo_ou_negativo(n):
    if int(n)<=0:
        print("N")
    else:
        print("P")


positivo_ou_negativo(5)


#faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre
# vendas expressa em porcentagem e
# custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o
# imposto sobre vendas.

def somaImposto(taxaImposto,custo):
    somatotal = int(custo)*(1+float(taxaImposto)/100)

    print(somatotal)


somaImposto(1,5000)
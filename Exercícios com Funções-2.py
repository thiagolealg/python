#Faça um programa para imprimir:
#
#        1
#        1   2
#        1   2   3
#        .....
#        1   2   3   ...  n
#
#    para um n informado pelo usuário.
#    Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def num_cascata2(n):
    for x in range(1,n+1):
        print(end ='\n')
        for y in range(1,x+1):
            print(y, end =' ')

num_cascata(5)
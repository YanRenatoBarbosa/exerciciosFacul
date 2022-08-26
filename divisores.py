#escreva um programa que leia um número inteiro positivo (n>1), que imprima seus divisores, a quantidade de divisores e se o número é primo

def divsores():
    numTarget = int(input('digite um número inteiro maior que 1: '))
    divisoresList = []
    numTargetEhPrimo = False

    while numTarget < 1:
        print('número deve ser maior que 1!!\n')
        numTarget = int(input('digite um número inteiro maior que 1: '))

    for i in range(1, numTarget + 1):
        if (numTarget % i == 0):
            divisoresList.append(i)

    print('Lista de divisores: ', divisoresList)
    print('Quantidade de divisores: ', len(divisoresList))

    if len(divisoresList) == 2:
        numTargetEhPrimo = True
        print('Este número é primo')

    else:
        print('Este número não é primo')






def fatoracaoDosPrimos():
    numTarget = int(input('Digite um número inteiro maior que 1: '))
    numPrimosList = []

    while numTarget < 1:
        print('número deve ser maior que 1!!\n')
        numTarget = int(input('digite um número inteiro maior que 1: '))


    for i in range(1, numTarget):
        #terminar em casa
        print("")

    print(numPrimosList)

fatoracaoDosPrimos()



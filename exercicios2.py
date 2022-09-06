def getNumber(enunciado):
    if enunciado == '':
        enunciado = 'Digite um número inteiro positivo: '

    num = int(input(enunciado))

    while num <= 0:
        print('\nO número deve ser maior que zero!!')
        num = int(input(enunciado))

    return num


def exercicio18():
    numtarget = getNumber('')
    resultadoSomatorio = 0

    for i in range(1, numtarget + 1):
        resultadoSomatorio += 2 * (i**2) + 3 * (i**3) + 4 * (i**4)

    print('\n\n', 'resultado:', resultadoSomatorio)

def exercicio19():
    numTarget = getNumber('')
    result = 0

    for i in range(1, numTarget + 1):
        if i % 2 != 0:
            result -= i
        else:
            result += i

    print('\nO resultado da operação é:',result)

def exercicio20():
    numTarget = getNumber('')
    result = 0

    divisoes = []

    for i in range(1, numTarget + 1):
        divNum = numTarget - (i - 1)

        if i == 1:
            divNum = numTarget

        elif i == numTarget:
            divNum = 1

        result += i / divNum
        divisoes.append('{} / {}'.format(i, divNum))

    print('O resultado é:', result)

    print('\n\nAs divisões feitas foram: ', divisoes)

def exercicio21():
    print('fms')

def exercicio22():
    ladoBase = getNumber('Digite o valor de um dos lados: ')
    ladoTopo = getNumber('Digite o valor do proximo lado: ')
    altura = getNumber('Digite o valor da altura: ')

    areaTrapezio = ((ladoBase + ladoTopo)*altura)/2

    print('A área do trapezio é:', areaTrapezio)

exercicio22()

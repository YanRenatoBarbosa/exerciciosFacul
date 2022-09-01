def exercicio14():
    vingadoresList = ['Homem de ferro', 'Capitão américa', 'Thor', 'Hulk', 'Viúva negra', 'Gavião arqueiro']

    vingadoresList.append('Homem-Aranha')

    print('\nLista inicial dos vingadores: ', vingadoresList)
    print('Indíce da lista do thor (começando pelo 0): {:1d}'.format(vingadoresList.index('Thor')))

    vingadoresList.remove('Viúva negra')
    vingadoresList.remove('Homem de ferro')

    print('\n\n\n',vingadoresList)
    print('Posição do Capitão américa: ', vingadoresList.index('Capitão américa'))

def exercicio15():
    def getNumber():
        num = int(input('Digite um número inteiro positivo: '))

        while num <= 0:
            print('\n\nO número precisa ser positivo!!')
            num = int(input('Digite um número inteiro positivo: '))

        return num

    print('Intervalo da lista')
    numInterval = getNumber()
    listNumbers = list(range(1, numInterval + 1))

    print('\nNúmero a ser verificado: ')
    numTarget = getNumber()

    print('\n----------')
    if numTarget in listNumbers:
        print('\nO número {:1d} está contido no intervalo de 1 à {:1d}'.format(numTarget, numInterval))
    else:
        print('\nO número {:1d} não está contido no intervalo de 1 à {:1d}'.format(numTarget, numInterval))


def exercicio16():
    intervalo = int(input('Digite um número inteiro positivo como intervalo: '))

    while intervalo <= 0:
        print('\n\nO número precisa ser positivo!!')
        intervalo = int(input('Digite um número inteiro positivo: '))

    initialList = list(range(1, intervalo))
    auxList = []

    for i in initialList:

        if (initialList[i - 1] % 2) != 0:
            auxList.append(initialList[i-1])

    print('Os número impares são: ', auxList)


def exercicio17():
    def getNumber(enunciado):
        if enunciado == '':
            enunciado = 'Digite um número inteiro positivo: '

        num = int(input(enunciado))

        while num <= 0:
            print('\n\nO número precisa ser positivo!!')
            num = int(input(enunciado))

        return num

    def getNotas(listNotas):
        for i in range(tamanhoTurma):
            notaAluno = getNumber('Digite a nota do aluno {:1d}: '.format(i + 1))
            listNotas.append(notaAluno)

    def getMedia(listNotas):
        media = 0
        for i in listNotas:
            listNotas += i

        media /= tamanhoTurma
        medias.append(media)

    print('Tamanho da turma')
    tamanhoTurma = getNumber('')

    notasP1 = []
    notasP2 = []
    medias = []

    print('\n\nDigite as notas dos alunos na P1!!')
    getNotas(notasP1)

    print('\n\nDigite as notas dos alunos na P2!!')
    getNotas(notasP2)

    print('\n\nMédias da P1 e P2 (respectivas):')
    getMedia(notasP1)
    getMedia(notasP2)

    print(medias)

exercicio17()

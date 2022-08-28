#escreva um programa que leia um número inteiro positivo (n>1), que imprima seus divisores, a quantidade de divisores e se o número é primo

def getNumber():
  numTarget = int(input('digite um número inteiro maior que 1: '))

  while numTarget < 1:
    print('número deve ser maior que 1!!\n')
    numTarget = int(input('digite um número inteiro maior que 1: '))

  return numTarget

def divisores():
  numTarget = getNumber()
  divisoresList = []
  numTargetEhPrimo = False

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
  numTarget = getNumber()
  numPrimosList = []

  for i in range(numTarget, 0, -1):
    divisoresCont = 0
    cont = 1

    while divisoresCont < 3 and cont <= i:
      if i % cont == 0:
        divisoresCont += 1
      cont += 1

    if divisoresCont == 2:
      numPrimosList.append(i)

  print(numPrimosList)

fatoracaoDosPrimos()

# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

div = 0
contdiv = 0
numero = int(input('Digite um numero: '))
for c in range(1, numero+1):
    div = numero % c
    if div == 0:
        contdiv = contdiv+1
if contdiv==2:
    print('Este numero é Primo! ele foi divisivel {} vezes!' .format(contdiv))
else:
    print('Este numero não é primo ele foi divisivel {} vezes' .format(contdiv))

    '''div = numero%c
    if div==0:
        contdiv =contdiv + 1
if contdiv==2:
    print('O numero digitado foi {} e ele é primo! ' .format(numero))


    elif contdiv < 1 or contdiv >2:
        print('O numero digitado foi {} e ele não é primo! ' .format(numero))'''
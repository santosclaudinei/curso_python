# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

c = tabuada = 0
while True:
    n = int(input('Digite o numero desejado: '))
    if n != -1:
        for c in range(1, 11, 1):
            tabuada = n * c
            print(f'{n} X {c} = {tabuada}')
            c += 1
    else:
        break
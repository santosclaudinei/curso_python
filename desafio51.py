# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

inicio = int(input('Digite o primeito termo: '))
if inicio != 0:
    limiar = inicio * 10
else:
    limiar = inicio + 20
razao = int(input('Digite a razão desejada: '))

for c in range(inicio, limiar, razao):
    print(c)


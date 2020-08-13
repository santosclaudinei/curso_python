# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior=0
menor=0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: ' .format(c)))
    if c == 1:
        maior = maior + peso
        menor = menor + peso
    if c > 1 and peso > maior:
        maior = peso
    if c > 1 and peso < maior:
        menor = peso
print('A pessoa mais pesada é {} e a menos pesada é {}!' .format(maior, menor))
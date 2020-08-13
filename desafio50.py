# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for c in range(1, 7):
  numero = int(input('Digite o {}º numero: '))
  if (numero % 2) == 0:
    soma = soma + numero
print('A soma de todos os numeros é {} :' .format(soma))
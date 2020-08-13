# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

acumulador = 0
soma = 0
for c in range(1, 501):
    divisivel = c % 3
    par = c % 2
    if divisivel == 0 and par != 0:
        acumulador = acumulador + 1
        soma = soma + c
print('A soma de todos os multiplos de 3 é {} e os numeros computados sao {}' .format(soma, acumulador))

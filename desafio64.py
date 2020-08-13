# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = 0
print("Digite 999 para encerrar o programa: ")
n = 0
para = 999
maior = menor = 0
while n != para:
    n = int(input('Digite um numero inteiro: '))
    if n != 999:
        cont += 1
        if n == 0:
            maior = n
            menor = n
        elif n > 1:
            if n > maior:
                maior = n
print('Foram digitados {} numeros.' .format(cont))
print('O maior numero é {}' .format(maior))

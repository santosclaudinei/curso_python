# desafio 38 - escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela
# uma mensagem: o primeiro valor é maior, o segundo valor é maior ou nao existe valor maior
# os dois sao iguais.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
if num1 > num2:
    print('Numero 1 é {} e numero 2 é {}. Numero 1 é maior que numero 2' .format(num1, num2))
elif num1 < num2:
    print('Numero 1 é {} e numero 2 é {}. Numero 2 é maior que numero 1' .format(num1, num2))
else:
    print('Numero 1 é {} e numero 2 é {}. Numero 1 é igual ao numero 2'.format(num1, num2))
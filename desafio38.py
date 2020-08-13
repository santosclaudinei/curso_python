# desafio 38 - escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
# o primeiro valor é maior, o segundo valor é maior ou nao existe valor maior os dois sao iguais.

numero1 = int(input('Digite o primeiro numero: '));
numero2 = int(input('Digite o segundo numero: '));
menor = 0;
maior = 0;

if (numero1 > numero2):
    maior = numero1;
    menor = numero2;
    print('o primeiro numero digitado foi {} e ele é maior que o segundo numero digitado que é {}' .format(numero1, numero2));
elif( numero2 > numero1):
    maior = numero2;
    menor = numero1;
    print('o segundo numero digitado foi {} e ele é maior que o primeiro numero digitado que é {}' .format(numero2, numero1));
else:
    print('Não existe um numero maior entre primeiro {} e o segundo {}. Os dois são iguais!' .format(numero1, numero2));
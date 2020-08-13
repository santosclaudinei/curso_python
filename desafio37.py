# desafio 37 - escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base
# de conversão: 1 para binario, 2 para octa e 3 para hexadecimal.

numero = int(input('Digite um numero: '));
print('''Escolha a opção desejada:
Digite [ 1 ] para converter para Binario
Digite [ 2 ] para coverter para Octal
Digite [ 3 ] para converter para Hexadecimal \n''')
opcao = int(input('Informe sua opção: '));

numconvertido = 0;
if (opcao == 1):
    numconvertido = bin(numero)
    print('O numero digitado foi {} e convertido para Binario ficou {}' .format(numero, numconvertido[2:]));
elif (opcao == 2):
    numconvertido = oct(numero);
    print('O numero digitado foi {} e oovertido para Octal ficou {}' .format(numero, numconvertido[2:]));
elif (opcao == 3):
    numconvertido = hex(numero);
    print('O numero digitado foi {} e convertido para Hexadecimal ficou {}' .format(numero, numconvertido[2:]));


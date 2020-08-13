# Escreva um programa que leia um numero inteiro qualquer e peça para que o usuario escolha
# qual sera a base de conversão.

numero = int(input('Digite um numero: '))
hexa = hex(numero)
binario = bin(numero)
octal = oct(numero)
opcao = str(input('Digite qual base voce gostaria de usar para a conversão: '))
if opcao == 'binario':
    print('A opção escolhida foi base binaria e o resultado é {}' .format(binario))
elif opcao == 'octal':
    print('A opção escolhida foi base octal e o resultado é {}'.format(octal))
elif opcao  == 'hexa':
    print('A opção escolhida foi base hexadecimal e o resultado é {}'.format(hexa))
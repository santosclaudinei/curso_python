# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
maior = 0
escolha = 0
while escolha != 5:
    print('''Escolha uma das opçoes no menu abaixo:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA''')
    escolha = int(input('Digite a opção desejada: '))
    if escolha == 1:
        resultado = n1 + n2
        print('A soma do {} com {} é igual a {}' .format(n1, n2, resultado))
    elif escolha == 2:
        resultado = n1 * n2
        print('A multiplicação de {} com {} é igual a {}'.format(n1, n2, resultado))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
            print('O maior numero entre {} e {} é {}' .format(n1, n2, maior))
        if n2 > n1:
            maior = n2
            print('O maior numero entre {} e {} é {}'.format(n1, n2, maior))
    if escolha == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
print('Fim do programa! Saindo')
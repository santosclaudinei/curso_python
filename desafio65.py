# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


cont = 0
contNum = 0
resposta = str
maior = menor = 0
while resposta != 'N':
    n = int(input('Digite um numero inteiro: '))
    resposta = input('Quer continuar digitando outro numero? \n[S] para SIM e [N] para NÃO: ').strip().upper()
    if n == 0:
        maior = n
        menor = n
    if n > 0:
        if n > maior:
            maior = n
            menor = maior
        if maior > n:
            maior = maior
            menor = n
    contNum += n
    cont += 1
media = contNum / cont
print('O maior numero digitado entre todos é {}' .format(maior))
print('O menor numero digitado entre todos é {}' .format(menor))
print('A media entre os numeros digitados é {}' .format(media))

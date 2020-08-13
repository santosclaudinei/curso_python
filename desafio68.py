# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
acertar = perder = 0

while True:
    n = int(input('Digite um numero: '))
    escolha = str(input('[P} para escolher Par e [I] para escolher Impar: ')).strip().upper()
    npc = randint(0, 10)
    resultado = n + npc
    if ((resultado % 2) == 0):
        vitoria = 'P'
    elif ((resultado % 2) == 1):
        vitoria = 'I'
    if escolha == vitoria:
        print('Voce venceu essa mão. Vamos tentar de novo.')
    else:
        print('Voce perdeu a mão. e o jogo vai se encerrar.')
        break
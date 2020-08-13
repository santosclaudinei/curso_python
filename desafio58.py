# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
tentativa = 0
numeropc = randint(0, 10)
acertou = False
numero = int(input('Digite um numero de 0 a 10: '))
while not acertou:
    if numeropc > numero:
        print('O numero é um pouco maior. Tente outra vez!')
        tentativa = tentativa+1
        numero = int(input('Digite um numero de 0 a 10: '))
    elif numeropc < numero:
        print('O numero é um pouco menor')
        tentativa = tentativa+1
        numero = int(input('Digite um numero de 0 a 10: '))
    elif numeropc == numero:
        acertou = True
        tentativa = tentativa+1
print('Voce acertou meu numero em {} tentativa(s).' .format(tentativa))
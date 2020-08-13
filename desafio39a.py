# Desafio 39 - faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua
# idade: se ele ainda vai se alistar, se é a hora de se alistar ou se ja passou do tempo de se alistar.
# seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Digite o ano de seu nascimento: '))
idade  = 2020 - ano
idadeAlistamento = 18
tempo = idadeAlistamento - idade
if idade == idadeAlistamento:
    print('Este é o ano de se alistar! Procure uma junta militar.')
elif idade > idadeAlistamento:
    print('Seu alistamento está em atraso. Procure URGENTE uma junta militar.')
else:
    print('Voce ainda nao pode se alistar, pois faltam {} anos.' .format(tempo))
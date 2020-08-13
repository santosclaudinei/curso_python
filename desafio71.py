# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cedula50 = cedula20 = cedula10 = cedula1 = 0
qtdnota50 = qtdnota20 = qtdnota10 = qtdnota1 = 0
cont = 0
valorSaque = int(input('Digite o valor desejado: Cedulas disponiveis R$ 1, R$ 10, R$ 20 e R$ 50: '))
cedula50 = valorSaque % 50
cedula20 = valorSaque % 20
cedula10 = valorSaque % 10
cedula1 = valorSaque % 1
while valorSaque != 0:
    if cedula50 < cedula20 and cedula50 < cedula10 and cedula50 < cedula1:
        qtdnota50 = cedula50
    elif cedula20 < cedula10 and cedula20 < cedula1:
        qtdnota20 = cedula20
    elif cedula10 < cedula1:
        qtdnota10 = cedula10
    else:
        qtdnota1 = cedula1
    break
print(f'Total de cedulas de 50 é {qtdnota50}')
print(f'Total de cedulas de 20 é {qtdnota20}')
print(f'Total de cedulas de 10 é {qtdnota10}')
if cedula1 != 0:
    print(f'Total de cedulas de 1 é {qtdnota1}')
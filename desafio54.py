# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maiorIdade = 0
menorIdade = 0
atual = date.today().year                                           #Pega o ano a partir da data do PC usando a biblioteca date
for c in range(1, 8):
    anoNascimento = int(input('Digite o ano de nascimento: '))
    idade = atual - anoNascimento
    if idade >= 18:
        maiorIdade = maiorIdade + 1
    else:
        menorIdade = menorIdade + 1
print('A quantidade de pessoas maiores de idade é {} e as que são menores de idade {}' .format(maiorIdade, menorIdade))
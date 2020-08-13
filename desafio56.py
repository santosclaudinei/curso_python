# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

contIdade = 0
maisVelho = 0
contF = 0
contM = 0
for c in range(1, 5):
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo: ')).upper()
    contIdade = contIdade + idade
    if(sexo == 'F'):
        contF = contF + 1
    if(sexo == 'M'):
        maior = idade
        nomeMV = nome
        contM = contM + 1
        if contM > 1:
            menor = maior
            maior = idade
media = contIdade / c
print('A media das idades é {}' .format(media))
print('O numero de mulheres é {}' .format(contF))
print('O homem mais velho é {} e sua idade é {}' .format(nomeMV, maior))

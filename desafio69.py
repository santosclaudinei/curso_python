# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

cont = contM = contF = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite qual o seu sexo: [M] para Masculino e [F} para Feminino: ')).upper().strip()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite qual o seu sexo: [M] para Masculino e [F} para Feminino: ')).upper().strip()
    if idade > 18:
        cont += 1
    if sexo == 'M':
        contM += 1
    if sexo == 'F':
        contF += 1
    escolha = str(input('Quer continuar [S] para SIM e [N] para NÃO: ')).strip().upper()
    while escolha != 'S' and escolha != 'N':
        escolha= str(input('Opção incorreta! Escolha novamente uma das opções: ')).upper().strip()
    if escolha == 'N':
        break
print(f'O numero de pessoas maiores de 18 anos é {cont}, o numero de homens {contM} e o de mulheres {contF} cadastrados.')
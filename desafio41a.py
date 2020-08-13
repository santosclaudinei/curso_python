# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

ano = int(input('Digite o ano de nascimeno'))
idade = 2020 - ano

if (ano < 9):
    print('O atleta possui {} anos e esta classificado na classe MIRIM!' .format(idade))
elif ((ano > 9 and ano < 14)):
    print('O atleta possui {} anos e esta classificado na classe INFANTIL!'.format(idade))
elif ((ano > 14 and ano < 19)):
    print('O atleta possui {} anos e esta classificado na classe JUNIOR!'.format(idade))
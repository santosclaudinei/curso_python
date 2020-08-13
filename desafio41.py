# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date

atual = date.today().year;
nascimento = int(input('Digite o ano em que nasceu: '));
idade = (atual - nascimento);

if (idade < 10):
    print('voce nasceu em {}, sua idade é {} e sua categoria é [MIRIM]' .format(nascimento, idade));
elif(15 > idade > 9):
    print('voce nasceu em {}, sua idade é {} e sua categoria é [INFANTIL]'.format(nascimento, idade));
elif (20 > idade > 14):
    print('voce nasceu em {}, sua idade é {} e sua categoria é [JUNIOR]'.format(nascimento, idade));
elif (25 > idade > 20):
    print('voce nasceu em {}, sua idade é {} e sua categoria é [SENIOR]'.format(nascimento, idade));
else:
    print('voce nasceu em {}, sua idade é {} e sua categoria é [MASTER]'.format(nascimento, idade));
# Desafio 39 - faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai se alistar, se é a hora de se alistar ou se ja passou do tempo de se alistar.
# seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date

anoatual = date.today().year;
datanascimento = int(input('Digite o ano em que nasceu: '));
idade = (anoatual - datanascimento);

if(idade < 18):
    print('Ainda não esta apto a se alistar! ');
    tempo = (18 - idade);
    if(tempo == 1):
        print('Voce atualmente tem {} e precisará se alistar no ano que vem! ' .format(idade));
elif(idade == 18):
    print('Chegou a hora de se alistar!!');
else:
    tempoamais = (idade - 18);
    print('Sua idade é {} anos Já se passaram {} anos do ano de alistamento.' .format(idade, tempoamais));
    print('Caso não tenha se alistado, favor comparecer a junta militar!');

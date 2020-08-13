# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO


n1 = float(input('Digite a nota da primeira unidade: '));
n2 = float(input('Digite a nota da segunda unidade: '));
n3 = float(input('Digite a nota da terceira unidade: '));
n4 = float(input('Digite a nota da quarta unidade: '));
media = ((n1 + n2 + n3 + n4)/4);

if (media < 5.0):
    print('Aluno [REPROVADO] por MEDIA! Até proximo ano. Espero que estude mais');
    print('Pois sua media foi {}' .format(media));
elif (media >= 5.0 and media < 7.0):
    print('Aluno em [RECUPERAÇÃO] pois não alcancou a media para ser aprovado.');
    print('A media alcancada foi {}' .format(media));
elif (media >= 7.0 and media <= 10.0):
    print('Parabens!!! Aluno [APROVADO] pois alcancou a media para ser aprovado.');
    print('A media alcancada foi {}'.format(media));
else:
    print('As notas digitadas estão invalidas. Verificar notas inseridas');
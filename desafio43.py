# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso: '));
altura = float(input('Digite a sua altura: '));
imc = (peso  / (altura * altura));

if (imc < 18.5 ):
    print('Seu peso é {}, sua altura é {} e seu IMC é {:.2f}' .format(peso, altura, imc));
    print('Você esta com peso e IMC ABAIXO DO IDEAL');
elif(25 > imc >= 18.5):
    print('Seu peso é {}, sua altura é {} e seu IMC é {:.2f}'.format(peso, altura, imc));
    print('Você esta no peso e IMC IDEAL');
elif(30 > imc >= 25):
    print('Seu peso é {}, sua altura é {} e seu IMC é {:.2f}'.format(peso, altura, imc));
    print('Você esta no peso e IMC no nivel de SOBREPESO');
elif(40 > imc >= 30):
    print('Seu peso é {}, sua altura é {} e seu IMC é {:.2f}'.format(peso, altura, imc));
    print('Você esta no peso e IMC no nivel de OBESIDADE');
else:
    print('Seu peso é {}, sua altura é {} e seu IMC é {:.2f}'.format(peso, altura, imc));
    print('Você esta no peso e IMC no nivel de OBESIDADE MORBIDA!!!');

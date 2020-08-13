# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso: '))
altuta = float(input('Digite sua altura: '))
imc = peso / (altuta * altuta)

print('De acordo com os dados digitados o seu peso é {}, sua altura é {} e seu IMC é {}' .format(peso, altuta, imc))
if imc < 18.5:
    print('Cuidado!!! Seu IMC esta muito baixo.')
elif imc >= 18.5 and imc < 25:
    print('Parabens!!! Seu IMC indica que você esta no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Voce esta com sobrepeso. favor procurar uma nutricionista!')
elif imc >= 30 and imc < 40:
    print('Voce precisa adotar habitos mais saudaveis, pois alcançou a obesidade.')
else:
    print('Voce corre risco de vida. procurar um medico e adotar habitos saudaveis alem de exercicios fisicos.')
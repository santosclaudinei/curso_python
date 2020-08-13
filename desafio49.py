# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

resultado = 0
numero = int(input('Digite o numero que deseja saber a tabuada: '))
for tabuada in range(1, 11, 1):
    resultado = numero*tabuada;
    print('O {} vezes {} é igual a {}' .format(numero, tabuada, resultado))
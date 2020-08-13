# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que
# tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

ladoA = int(input('Digite um valor para o lado A do triangulo: '))
ladoB = int(input('Digite um valor para o lado B do triangulo: '))
ladoC = int(input('Digite um valor para o lado C do triangulo: '))

if (ladoA == ladoB and ladoA == ladoC and ladoB == ladoC):
    print('obtivemos que Lado A é {}, Lado B é {} e Lado C é {} \nCom isso contatamsos que o triangulo é do tipo EQUILATERO!' .format(ladoA, ladoB, ladoC))
elif (ladoA != ladoB and ladoA != ladoC and ladoB != ladoC):
    print('obtivemos que Lado A é {}, Lado B é {} e Lado C é {} \nCom isso contatamsos que o triangulo é do tipo ESCALENO!'.format(ladoA, ladoB, ladoC))
else:
    print(
        'obtivemos que Lado A é {}, Lado B é {} e Lado C é {} \nCom isso contatamsos que o triangulo é do tipo ISOCELES!'.format(ladoA, ladoB, ladoC))

# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

lado1 = float(input('Informe a medida para esse lado do trinagulo: '));
lado2 = float(input('Informe a medida para esse lado do trinagulo: '));
lado3 = float(input('Informe a medida para esse lado do trinagulo: '));

if((lado2 + lado3) > lado1) and ((lado1 + lado3) > lado2) and ((lado1 + lado2) > lado3):
    print('As medidas informadas permitem formar um triangulo!');
    if((lado1 == lado2) and (lado1 == lado3)):
        print('O triangulo formado pelos lados {}, {} e {} formam um do tipo [EQUILATERO]' .format(lado1, lado2, lado3));
    elif(lado1 != lado2) and (lado2 != lado3):
        print('O triangulo formado pelos lados {}, {} e {} formam um do tipo [ESCALENO]' .format(lado1, lado2, lado3));
    else:
        print('O triangulo formado pelos lados {}, {} e {} formam um do tipo [ISOCELES]' .format(lado1, lado2, lado3));

else:
    print('As medidas informadas não permitem formar um triangulo!');

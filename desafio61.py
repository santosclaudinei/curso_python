# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while
contador = 1
inicio = int(input('Digite o numero para iniciar nossa progressão aritimetica: '))
termo = inicio
razao = int(input('Digite a razão para iniciar nossa progressão aritimetica'))
while contador < 11:
    print('{}' .format(termo), end=' ')
    print('-> ' if contador > 0 and contador < 10 else '.',end='' )
    termo = termo + razao
    contador = contador + 1
   

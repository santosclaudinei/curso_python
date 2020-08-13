# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

total = 0
opcao = 10
contador = 1
inicio = int(input('Digite o numero para iniciar nossa progressão aritimetica: '))
termo = inicio
razao = int(input('Digite a razão para iniciar nossa progressão aritimetica'))
while opcao != 0:
    total = total + opcao
    while contador < total+1:
        print('{}'.format(termo), end=' ')
        print('-> ' if contador > 0 and contador < 10 else '.', end='')
        termo = termo + razao
        contador = contador + 1
    print('\nPAUSA!!!')
    opcao = int(input('\nDigite quantos termos a mais gostaria de visualizar: '))
print('A quantidade de termos informados foram {}'.format(total))


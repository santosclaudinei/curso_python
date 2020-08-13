# Exercicio Python 063: Escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N primeiros
# Elementos de uma sequencia de fibonacci.

n = int(input('Digite a quantidade de termos que deseja: '))        #Pede que o usuário digite um numero
anterior = 1
atual = 0
print('A sequencia de FIBONACCI desejada:')
print('{} -> {} ' .format(atual, anterior), end='')                 #Imprime o atual e o anterior.
t = 2                                           #Define um contador
while t != n:                                   #Enquanto não chegar a quantidade desejada pelo usuario percorre o laço
    t3 = atual + anterior
    print('-> {}' .format(t3), end=' ')
    atual = anterior                            #Guarda o valor de anterior para que seja utilizado na soma da linha 10.
    anterior = t3                               #Guarda o valor de t3 para que seja utilizado na soma da linha 10.
    t += 1                                      #Incrementa o contador para mostrar a quantidade de numeros correta.

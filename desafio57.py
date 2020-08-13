# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo: ')).upper().strip()
while sexo not in 'MF':                                         #Enquanto sexo for diferente das duas opções. pede que digite denovo
    sexo = str(input('Digite seu sexo: ')).upper().strip()
print('Sexo {} registrado com sucesso! ' .format(sexo))


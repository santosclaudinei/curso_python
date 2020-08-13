# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()    #Retira os espacos no inicio e no fim e coloca todas as letras em maiusculas
palavra = frase.split()                                     #Separa as palavras em conjuntos. ex: [OLA] [MUNDO]
junto = ''.join(palavra)                                    #Junta as palavras removendo os espacos entre elas.
invertida = ''
for letra in range(len(junto)-1, -1, -1):                   #Percorre o tamanho da palavra junto de tras pra frente
    invertida = invertida + junto[letra]                    #Invertida recebe as letras de tras pra frente. ai ocorre a inversao da palavra digitada
print(junto, invertida)                                     #Imprime a frase digitada sem espacos da forma normal e invertida.
if junto == invertida:                                      #Faz a condicao para verificar se é palindromo
    print('É Palindromo!')
else:                                                       #Faz a condicao para informar caso nao seja palindromo
    print('Não é palindromo!')
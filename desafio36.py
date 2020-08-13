#Escreva um programa para provar o emprestimo bacario para a compra de uma casa. o programa vai perguntar o valor da casa,
#o salario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou entao o emprestimo sera negado.

valor_casa = float(input('Qual o valor da casa desejada: '));            #Solicita que o usuario informe o valor da casa
salario = float(input('informe o salario do funcionario: '));             #Solicita que o funcionario digite seu salario
parcelas_casa = float(input('Em quantas parcelas voce deseja parcelar: ')); #Informa o numero de parcelas
prestacao_casa = (valor_casa/parcelas_casa);
percente_salario = (salario * 0.30);

if (prestacao_casa > percente_salario):
        print('A prestação esta muito alto. Dessa forma você não conseguirá honrar o compromisso. EMPRESTIMO NEGADO!')
elif (prestacao_casa == percente_salario):
        print('A prestação esta muito alto. Dessa forma você não conseguirá honrar o compromisso. EMPRESTIMO NEGADO!')
else:
   print('Você possui todas as condicoes ideais para honrar o compromisso. EMPRESTIMO CONCEDIDO!')

print( 'O numero de prestações foi {}, o percentual de 30% do seu salario é de {:.2f} ' .format(parcelas_casa, percente_salario));
print( 'e o percentual minimo para aprovacao do emprestimo corresponde a salario é {:.2f} !' .format(prestacao_casa));
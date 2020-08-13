# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

precoproduto = float(input('Informe o valor do produto: '));
print('''Entre com a forma de pagamento desejada: ');
1 - para [DINHEIRO OU CHEQUE]
2 - para [A VISTA NO CARTÃO]
3 - para [2X NO CARTÃO]
4 - para [3X OU MAIS NO CARTÃO] ''');
modopagamento = int(input('Digite sua opção: '))

if modopagamento == 1:
    valorfinal = precoproduto - (precoproduto * 0.10);
elif modopagamento == 2:
    valorfinal = (precoproduto - (precoproduto * 0.05));
elif modopagamento == 3:
    valorfinal =+ precoproduto;
    parcela = valorfinal / 2;
    print('O valor total da compra foi {} que foi dividido em 2x e ficou dividido em 2 parcelas de {}' .format(valorfinal, parcela))
elif modopagamento == 4:
    dividido = int(input('Digite a quantidade de parcelas que voce deseja dividir a compra: '))
    valorfinal = (precoproduto + (precoproduto * 0.20));
    parcela = valorfinal / dividido;
    print('O valor total da compra foi {} que foi dividido em {}x com parcelas de {}'.format(valorfinal, dividido, parcela))
print ('O valor normal do produto é {:.2f}, a opcão escolhida foi {} e o valor final é {:.2f}' .format(precoproduto, modopagamento, valorfinal));


'''else:
    print ('Essa opção é invalida! Tente novamente!');'''

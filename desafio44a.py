# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valorProduto = float(input('Digite o valor do Produto: '))
condicaoPagamento = int(input('1 -> A vista (Dinheiro/Debito) \n2 -> A vista no Cartão \n3 -> 2X no cartão \n4 -> 3X ou Mais \nEscolha a forma de pagamento desejada: '))

if condicaoPagamento == 1:
    valorfinal = valorProduto - (valorProduto * 0.10)
    print('A opção escolhida foi dinheiro ou debito dessa forma produto era {} e saiu por {}' .format(valorProduto, valorfinal))
elif condicaoPagamento == 2:
    valorfinal = valorProduto - (valorProduto * 0.05)
    print('A opção escolhida foi dinheiro ou debito dessa forma produto era {} e saiu por {}'.format(valorProduto,valorfinal))
elif condicaoPagamento == 3:
    valorfinal = valorProduto
    print('A opção escolhida foi dinheiro ou debito dessa forma produto era {} e saiu por {}'.format(valorProduto,valorfinal))
elif condicaoPagamento == 4:
    valorfinal = valorProduto + (valorProduto * 0.20)
    print('A opção escolhida foi dinheiro ou debito dessa forma produto era {} e saiu por {}'.format(valorProduto,valorfinal))

# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

qtdProduto = cont = totalPreco = maisDemil = menorPreco = produtoBarato = 0
while True:
    nomeProduto = str(input('Digite o nome do produto: ')).strip()
    precoProduto = float(input('Digite o preco do produto: '))
    escolha = str(input('Digite [S] para CONTINUAR e [N] para ENCERRAR o programa: ')).upper().strip()
    totalPreco += precoProduto
    if precoProduto > 1000:
        qtdProduto += 1
    if cont == 0:
        menorPreco = precoProduto
    if cont > 0:
        if menorPreco < precoProduto:
            menorPreco = menorPreco
            produtoBarato = nomeProduto
        elif menorPreco > precoProduto:
            menorPreco = precoProduto
            produtoBarato = nomeProduto
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('Digite [S] para CONTINUAR e [N] para ENCERRAR o programa: ')).upper().strip()
    if escolha == 'N':
        break
    cont += 1
print(f'O total gasto em produtos é {totalPreco}')
print(f'A quantidade de produtos comprados é {qtdProduto}')
print('O produto de menor preco é {}' .format(produtoBarato))
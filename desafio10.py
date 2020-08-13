dinbolso = (float(input('digite quanto você tem no bolso:' )))              #Variavel que recebe a quantidade de dinheiro que o usuario tem no bolso.
dolar = (float(3.27))                                                       #Variavel que recebe o valor do dolar atualizado.
meudolar = (float(dinbolso / dolar))                                        #Variavel que faz o calculo, converte para real e informa o valor convertido.
print ('\nNo meu bolso tenho R$ {}' .format(dinbolso))                      #Mostra o valor que o usuario tem no bolso.
print ('E o dolar hoje vale U$$ {}' .format(dolar))                         #Mostra o valor do dolar atualizado.
print ('Dessa forma só posso comprar U$$ {:.2f}' .format(meudolar))         #Mostra o valor que foi convertido de real para dolar.
       
       

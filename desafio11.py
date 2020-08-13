altura = float(input('digite a altura da parede que deseja pintar: '))                                      #Solicita que o usuario digite a altura da parede a ser pintada
largura = float(input('digite a largura da parede que deseja pintar: '))                                    #Solicita que o usuario digite a largura da parede a ser pintada
dimensao = altura * largura                                                                                 #Realiza o calculo da área total a ser pintada
ldt = dimensao / 2                                                                                          #Realiza o calculo de quantas latas de tintas serão necessarias

print ('\nA altura da parede é {} e a largura é {}' .format(altura, largura))                               #Imprime na tela a altura e largura digitadas
print ('A dimensão da área é {} metros²' .format(dimensao))                                                 #Imprime a dimensão total a ser pintada
print ('A quantidade de latas de tintas \nnecessarias para pintar essa área é {}' . format(ldt))            #Imprime a quantidade de latas de tintas necessarias

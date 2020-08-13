salario = float(input('informe o salario do funcionario: '))            #Solicita que o funcionario digite seu salario
reajuste = (salario + ((salario * 15)/100))                             #Calcula o novo salario do funcionario

print ('O salario do funcionario é R$ {}' .format(salario))             #Imprime na tela o salario digitado pelo funcionario
print ('O novo salario do funcionario é R$ {}' .format(reajuste))       #Imprime na tela o novo salario digitado do funcionario

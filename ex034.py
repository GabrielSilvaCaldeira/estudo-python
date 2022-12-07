# Aumento mútiplo

salario = float(input('Digite o valor do salário: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100) #salário + o reajuste (salário * 15 dividido por 100)
else:
    novo = salario + (salario * 10 / 100)
print('O reajuste do salário foi de R${:.2f} para R${:.2f}'.format(salario, novo))
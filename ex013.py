#Reajuste salarial

valor = float(input('Digite o valor do salário: R$'))
r = int(input('Digite a porcentagem do reajuste: '))
a = (valor * r) / 100
b = valor + a
print('Com o aumento de {}% no reajuste o salário de R${:.2f} vai para R${:.2f}'.format(r, valor, b))
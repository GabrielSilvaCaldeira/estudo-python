# Aprovando emprestimo

casa = float(input("Digite o valor do imovel: R$"))
parcela = int(input('Digite a quantia de parcelas: x'))
valorp = casa / parcela
print('O valor de cada parcela sera de R${:.2f}'.format(valorp))
salario = float(input('Digite o valor do salário: R$'))
minimo = salario * 50 / 100
if valorp <= minimo:
    print('Emprestimo \033[0;33;0mAPROVADO!\033[m')
else:
    print('Emprestimo NÃO APROVADO! renda mensal muito abaixo')
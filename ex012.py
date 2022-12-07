#Calculando desconto

preço = float(input('Digite o preço do produto: R$'))
d = int(input('Digite o desconto: %'))
a = (preço * d) / 100
b = preço - a
print('Com {}% de desconto o valor de R${:.2f} vai para: R${:.2f}'.format(d, preço, b))
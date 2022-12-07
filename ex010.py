#Conversor de moedas

real = float(input('Coloque o valor: R$'))
d = real / 4.85
e = real / 5.33
b = real / 206380.62
print('com R${:.2f} você pode comprar: \nUS$ {:.2f} \nEUR$ {:.2f} \nBitcoin {:.2f}'.format(real, d, e, b))
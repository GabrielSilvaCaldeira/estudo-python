d = int(input('Dias alugados: '))
k = int(input('KM rodados: '))
a = (d * 60) + (k * 0.15)
print('Pelos {} dias alugado e {}KM rodados o valor final foi de R${:.2f}'.format(d, k, a))
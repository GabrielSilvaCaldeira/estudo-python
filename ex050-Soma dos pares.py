soma = 0
cont = 0
for n in range(1, 6):
    num = int(input('Digite o {}° valor: '.format(n)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('*-100')
print('O resultado soma dos {} números pares informados é: {}'.format(cont, soma))
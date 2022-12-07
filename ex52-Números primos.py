n = int(input('Digite um valor: '))
t = 0
for c in range(1, n, +1):
    if n % c == 0:
        print('\033[34m', end='')
        t += 1
    else:
        print('\033[37m', end='')
    print('{}'.format(c, end=''))
print('\033[mO número {} foi divisível {} vezes.'.format(n, t))
if t == 2:
    print('{} Não é um número primo'.format(n))
else:
    print('{} É um número primo'.format(n))

num = int(input('Digite um valor para vêr sua tabuada: '))
for n in range(1, 101):
    print('{} X {:2} = {}'.format(num, n, num*n))
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 < n2:
    print('{} é o maior'.format(n2))
elif n2 < n1:
    print('{} é o maior'.format(n1))
else:
    print('Não existe maior ou menor')
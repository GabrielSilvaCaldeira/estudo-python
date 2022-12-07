termo = int(input('Primeiro termo: '))
razao = int(input('A Razão: '))
decimo = termo + (10-1) * razao
for n in range(termo, decimo + razao, razao):
    print('{}'.format(n), end=' > ')
print('FIM!')
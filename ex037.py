
num = int(input('Digite um valor de entrada: '))
print('''Escolha um tipo de conversão
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL
''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} foi convertido para BINÁRIO: {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} foi convertido para OCTAL: {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} foi convertido para HEXADECIMAL: {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida')
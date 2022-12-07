p1 = int(input('Informe o primeiro lado: '))
p2 = int(input('Informe o segundo lado: '))
p3 = int(input('Informe o terceiro lado: '))

if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('{}, {} e {} formam um triângulo '.format(p1, p2, p3), end='')
    if p1 == p2 == p3:
        print('EQUILÁTERO : lados iguais')
    elif p1 != p2 != p3 != p1:
        print('ESCALENO : todos os laods diferentes')
    else:
        print('ISÓSCELES : apenas um lado diferente')
else:
    print('{}, {} e {} NÃO podem formar um triângulo'.format(p1, p2, p3))
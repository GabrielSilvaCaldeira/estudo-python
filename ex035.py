# Triângulo 1.0v

a = float(input('Primeiro segmento: '))
b = float(input('Segunado segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos {} {} {} formam um triângulo'.format(a, b, c))
else:
    print('Os segmentos {} {} {} NÂO formam um triângulo'.format(a, b, c))
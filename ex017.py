#Cateto e Adjacente
#Opção 01

'''co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da Hipotenusa é de: {:.2f}'.format(hi))'''

#Opção 02

import math
co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
hi = math.hypot(co, ca)
print('O valor da Hipotenusa é {:.2f}'.format(hi))
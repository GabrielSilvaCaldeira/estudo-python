# Maior e Menor valor

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# identificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# identificando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor número é o {} e o maior é o {}'.format(menor, maior))

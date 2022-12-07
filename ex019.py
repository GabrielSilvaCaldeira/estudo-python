# Sorteando um item da lista

import random
n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))
lista = [n1, n2, n3, n4]
escolher = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolher))

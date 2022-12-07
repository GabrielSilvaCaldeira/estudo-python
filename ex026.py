n = str(input('Qual seu nome: ')).upper().strip()
print('A letra A apareceu {} vezes'.format(n.count('A')))
print('A letra A apareceu pela primeira vez na posição {}'.format(n.find('A')+1))
print('A letra A apareceu pela ultima vez na posição {}'.format(n.rfind('A')+1))
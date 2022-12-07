#Calcular a parede

larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
a = larg * alt
print('Com a dimensão de {}x{} sua área é {}m²'.format(larg, alt, a))
tin = a / 4
print('Você precisara de {}L de tinta'.format(tin))
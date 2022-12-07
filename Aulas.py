# AULA 12 : Condicionais aninhadas
#se - if
#senão se - elif
#senão - else

#Exemplo

num = int(input('Digite o número: '))
if num == 0:
    print('O número {} e NULO'.format(num))
elif num %2:
    print('O númro {} é ÍMPAR'.format(num))
else:
    print('O número {} é PAR'.format(num))



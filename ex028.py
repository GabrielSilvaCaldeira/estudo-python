from random import randint
from time import sleep
comput = randint(0, 10) # Computador pensa em um número
print('_' * 50)
print('Adivinhe o número que estou pensando de 0 a 10: ')
print('_' * 50)
jog = int(input('Responda: ')) # Resposta do jogador
print('PROCESSANDO...')
sleep(3)
if jog == comput:
    print(' {} PARABÉNS! você ganhou =)'.format(comput))
else:
    print('VOCÊ PERDEU =(... Eu pensei no número {} e não no {} '.format(comput, jog))
print('_' * 50)
from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('Suas opções:'
      '[0] pedra  '
      '[1] papel  '
      '[2] tesoura  ')

jogador = int(input('Qual é a sua jogada? : '))
print('=' * 30)
print(' Você jogou {}'.format(itens[jogador]))
print(' O computador jogou {}'.format(itens[computador]))
print('=' * 30)

# CONDIÇÃO CONFORME A ESCOLHA DE AMBOS.

if computador == 0: # pedra
    if jogador == 0:
        print('\033[37mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    else:
        print('\033[31mINVALIDO!\033[m')

elif computador == 1: # papel
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[37mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCEU!\033[m')
    else:
        print('\033[31mINVALIDO!\033[m')

elif computador == 2: # tesoura
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[37mEMPATE!\033[m')
    else:
        print('\033[31mINVALIDO!\033[m')

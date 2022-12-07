from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano em que nasceu: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos de idade atualmente'.format(nascimento, idade))
if idade < 18:
    saldo = 18 - idade
    print('faltam {} anos para você se alistar.'.format(saldo))
elif idade == 18:
    print('Você está na idade certa para se alistar')
else:
    saldo = idade - 18
    print('já se passaram {} anos de sua idade ideal para seu alistamento,'
          ' tente se alistar o mais rápido possível!'.format(saldo))
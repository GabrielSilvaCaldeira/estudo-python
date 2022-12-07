# Ano bissexto

from datetime import date
ano = int(input('Digite o ano que quer ou digite "0" para ano atual: '))
if ano == 0:#se o ano for 0
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #Divisivel por 4 = 0 / divisivel por 100 != 0
    print('O ano de {} é Bissexto'.format(ano))
else:
    print('O ano de {} não é Bissexto'.format(ano))
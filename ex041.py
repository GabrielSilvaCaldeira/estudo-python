from datetime import date
atual = date.today() .year
idade = int(input('Digite a data em que o atleta nasceu: '))
data = atual - idade
if data  < 6:
    print('O atleta tem {} anos, é muito novo para participar!'.format(data))
elif data <= 9:
    print('O atleta tem {} anos, competira na categoria MIRIM'.format(data))
elif data <= 14:
    print('O atleta tem {} anos, competira na categoria INFANTIL'.format(data))
elif data <= 19:
    print('O atleta tem {} anos, competira na categoria JÚNIOR'.format(data))
elif data <= 24:
    print('O atleta tem {} anos, competira na categoria SÊNIOR'.format(data))
else:
    print('O atleta {} anos, competira na categoria MASTER'.format(data))

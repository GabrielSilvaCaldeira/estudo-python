#Custo de viajem

# 1° opção

'''distancia = float(input('Qual a distancia de sua viagem ? '))
print('Sua viagem é de {:.2f}KM'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.49
print('O valor de sua viagem é de R${:.2f} por KM'.format(preço))'''

# 2° opção

distancia = float(input('Qual a distancia dde sua viagem ? '))
print('Sua viagem é de {:.2f}KM'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.49
print('O valor de sua viagem é de R${:.2f}'.format(preço))

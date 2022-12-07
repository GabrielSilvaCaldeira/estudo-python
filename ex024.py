# Verificando as primeiras letras do texto

# 1°

c: str = str(input('Digite o nome da cidade: ')).strip().split()
print(c[:6].upper() == 'SANTO')

#2°

'''cidade = str(input('Digite o nome de sua cidade:  ')).strip().casefold().split()
print(f'Essa cidade começa com Santo? {"santo" == cidade[0]}.  ')
'''
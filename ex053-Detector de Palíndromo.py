frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.strip()
junto = ''.join(palavras)
inverso = ''
for l in range(len(junto) -1, -1, -1):
    inverso += junto [l]
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('Não temos um Palíndromo')
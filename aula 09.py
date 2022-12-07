# Manipulando texto

frase = 'abcdefghijklmnopqrsvuxywz'

#selecional do {} ao {} pulando de {}
print (frase[0:16])

#Print do texto formatado
print("""Aprenda as habilidades necessárias para fazer jogos, animações e aplicativos.
Descubra como hackear sua própria educação. Desenvolva as habilidades necessárias no Séc. XXI. Com essa trilha você vai se encontrar no universo da programação. 
Aprenda a programar. Programe para aprender.""")

#Contar quantas vezes a letra se repete
print(frase.count('b'))

#Mudando a palavra
frase = frase.replace('abcde', 'foi')
print(frase)

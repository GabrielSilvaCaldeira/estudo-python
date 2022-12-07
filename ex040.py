nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('Média {} aluno APROVADO!'.format(media))
elif media <= 5.0:
    print('Média {} aluno REPROVADO!'.format(media))
else:
    print('Média {} aluno de RECUPERAÇÃO!'.format(media))
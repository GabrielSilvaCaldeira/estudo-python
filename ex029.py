vel = float(input('Qual a velocidade: '))

if vel > 70:
    print('ATENÇÃO: você está em uma velocidade acima do permitido da via (70KM/h), por isso será multado!')
    multa = (vel - 70) * 7
    if vel > 70:
       pontos = (vel > 70) + 5

    print('O valor aplicado é de R$ {:.2f} e a pontuação é de {} pontos'.format(multa, pontos))
else:
    print('Velocidade aceitavel, Dirija com cuidado!')
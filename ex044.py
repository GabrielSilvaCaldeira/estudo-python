print('{:=^80}'.format(' CAROLINE STYLE '))

preço = float(input('Digite o valor da compra: R$ '))
print('''Formas de pagamento
[ 1 ] à vista no dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2X no cartão: preço formal
[ 4 ] em 3X ou mais no cartão: 20% DE JUROS''')
opçao = int(input('Qual a forma de pagamento: '))

if opçao == 1:
    total = preço - (preço * 10 / 100)
    print(' O valor da compra é de: R$ {:.2f}\n com o desconto de 10% o valor fica por: R$ {:.2f}'.format(preço, total))
elif opçao == 2:
    total = preço - (preço * 5 / 100)
    print(' O valor da compra é de: R$ {:.2f}\n com o desconto fica por: R$ {:.2f}'.format(preço, total))
elif opçao == 3:
    total = preço
    parc = total / 2
    print(' O valor da compra é de: R$ {:.2f}\n cada parcela saíra por: R${:.2f}'.format(total, parc))
elif opçao == 4:
    parcelas = int(input('Quantas parcelas: '))
    if parcelas == 2:
        parc = preço / 2
        print('O valor da compra é de: R$ {:.2f}\n cada parcela saíra por: R${:.2f}'.format(preço, parc))
    elif parcelas <2:
        total = preço - (preço * 5 / 100)
        print(' O valor da compra é de: R$ {:.2f}\n com o desconto fica por: R$ {:.2f}'.format(preço, total))
    else:
        total = preço + ( preço * 20 / 100)
        valor = total / parcelas
        print(' O valor da compra é de: R$ {:.2f}\n a opção de pagamento foi em {}X de R${:.2f} cada no cartão\n '
          'com o juros de 20% ficou por: R${:.2f}'.format(preço,parcelas,valor, total))

else:
    total = preço
    print('Opção invalida. tente novamente ')


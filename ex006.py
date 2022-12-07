#Crie um código que mostre o dobro, triplo e raiz quadrada do valor dado

n = float(input("Digite o valor: "))
a = n * 2
b = n * 3
c = n ** (1/2)
print("O dobro do valor {} é {} \nO triplo {}".format(n, a, b))
print("A raiz quadrada do valor {} é {:.3f}".format(n, c))
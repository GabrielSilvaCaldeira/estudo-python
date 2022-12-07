#comando para relatar informações de entrada de dados
a = input("Digite algo: ")
print('O tipo primitivo desse valor é: ', type(a))
print('É um espaço vázio: ', a.isspace())
print('É um alfabeto: ', a.isalpha())
print('É um número: ', a.isnumeric())
print('É um alfanumérico: ', a.isalnum())
print('É maiúsculo: ', a.isupper())
print('É minúsculo: ', a.islower())
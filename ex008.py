#Conversor de medidas/Modelo 1

#medida = float(input('Digite o valor em metros: '))
#mm = medida * 1000
#cm = medida * 100
#dm = medida * 10
#dam = medida / 10
#hm = medida / 100
#km = medida / 1000
#print("A medida de {} corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm".format(medida, km, hm, dam, dm, cm, mm))

#Modelo 2

m = float(input('Uma distancia em metros: '))

print('A medida de {} corresponde a \n {} km \n {} hm \n {} dam \n {} dm \n {} cm \n {} mm '.format(m,m/1000,m/100,m/10,m*10,m*100,m*1000))

# == -> SI le importa el valor

print(True == 1) #True
print('' == 1) #False
print([] == 1)#False
print( 10 == 10.0) #True
print( [] == [] ) #True

# is -> NO le importa el valor, solo le importa el valor de la MEMORIA

print([] is []) 

lista1 = [1,2,3]
# lista2 = lista1[:]
lista2 = lista1

print( lista2 is lista1)
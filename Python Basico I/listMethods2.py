
#index
lista = [1,2,3,4,5]
print(lista.index(2))
print(lista.index(3, 0, 5)) #Para buscar en un rango.

#in

lista2 = ['a','d','c','d','e']

inVariable = 'x' in lista2

print(inVariable)

#count
countVariable = lista2.count('d')
print(countVariable)


#sort 
lista3 = ['a','d','c','d','e','c','f','z']

ordenar = lista3[:]
ordenar.sort() #Modifica la original
print(ordenar)

#sorted
lista4 = ['a','d','c','d','e','c','f','z']

ordenar2 = sorted(lista4)
print(lista4)

#copiar lista
nueva_Lista4 = lista4.copy() # lista4[:]
print(nueva_Lista4)

#reverse
nueva_Lista4.reverse() #Modifica la original [::-1]
#nueva_lista4[::-1]
print(nueva_Lista4)

#Sets
#Es una estructura de datos. 
# Colección ordenada de objetos únicos. (No hay valores duplicados)

my_set = {2,3,4,5,7,1,5,2,3,2,4,1,5,5}
#print(my_set)

#add
#my_set[0] = 100; #SON INMUTABLES
print(my_set)
my_set.add(9)
my_set.add(7)

#print(my_set)



#Listas a sets
lista = [2,3,4,5,7,1,5,2,3,2,4,1,5,5]
lista_set = list(set(lista))
print(lista)
print(lista_set)


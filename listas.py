
lista = [1,2,3,4,5]
lista2 = ['a','b','c','d','e']

lista3 = [1,2,'a', True, False]

#Una lista es una esctructura de datos. 

#List Slicing

carrito = [
    'cuaderno',
    'lentes',
    'juguetes',
    'uvas'
]

print(carrito)
print(carrito[0:2]) #Crean una nueva lista
print(carrito)

#Las listas si son mutables. 

carrito[0] = 'Laptop'
print("Carrito1: ",carrito)

#Copiar 
carrito2 = carrito #Copia la referencia en la memoria 0x023BA
print("Carrito2: ", carrito2)
carrito2[1] = "Xbox"
print("Carrito2: ", carrito2)
print("Carrito1: ",carrito)

#¿Cómo copiamos una lista?
carrito3 = carrito[:] #Crea una lista nueva con memoria nueva

print("Carrito 3: ",carrito3)
carrito3[1] = 'Play'
print("Carrito 3: ",carrito3)
print("Carrito2: ", carrito2)
print("Carrito1: ",carrito)

#Iterable es un objeto o colección que se itera o repite

#lista, tuple, set, string, diccionarios 

usuario = {
    'name': 'Luisa',
    'edad': 15,
    'ejercicio': True
}

#Puedes usar los metodos .items(), .keys(), .values()
# for item in usuario.items():
#     key, value = item #Desestructuramos. 
#     print(item)
#     print(f"Llave: {key}")
#     print(f"Valor: {value}")
    
for key, value in usuario.items():
    print(f"Llave: {key}")
    print(f"Valor: {value}")
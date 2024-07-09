
usuario = {
    'nombre': 'Luisa',
    'numeros_suerte': [1,2,3],
    'edad': 27
}
#get
print(usuario.get('edad', 30))


#in
print('numeros_suerte' in usuario)
print('numeros_suerte' in usuario.keys())
print('numeros_suerte' in usuario.values())

#items
print(usuario.items())

#clear
#usuario.clear()
print(usuario)

#Copy
usuario2 = usuario.copy()
print(usuario2)

#Pop 
# [1,2,3] .pop()
usuario2.pop('nombre')
print(usuario2)

# usuario2.popitem()
# print(usuario2)

#update
usuario2.update({'numeros_suerte': [5,6,7,8], 'edad': 28})
print(usuario2)

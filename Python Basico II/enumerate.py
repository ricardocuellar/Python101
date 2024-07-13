# Enumerate -> Enumerar 
# Strings y Listas 
# Ayuda a crear una llave y un valor (Key -> Value)

# for i,char in enumerate('Luisa'):
#     print(i,char) 

# lista = [1,2,3,4,5,6,7,8,9,10]

# for perrito,gatito in enumerate(lista):
#     print(perrito,gatito) 


for i,char in enumerate(list(range(100))):

    if char == 27:
        print(f'Edad de Luisa: {i}')
    else:
        print(i,char)
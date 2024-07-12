
#Operadores lógicos:
# >, <, ==, and, or, not

#Ejercicio 
# Personaje mágico y/o experto y/o espadachín.
# Magico y Experto y XXXXX = Tu eres el maestro magico experto de 'X' cosa
# Magico y XXXXX = Tu eres el maestro magico 'X' cosa
# Experto y XXXXX = Tu eres el maestro experto de 'X' cosa


print('''Elección de personaje:

    Responda de la siguiente manera
    Sí: 1
    No: 0
''')

p_magico = int(input("¿Desea que su personaje sea mágico?: "))
p_experto = int(input("¿Desea que su personaje sea experto?: "))
p_espadachin = int(input("¿Desea que su personaje sea espadachín?: "))
personajes = [p_magico, p_experto, p_espadachin]
personajes_value = ["magico", "experto", "espadachin"]



# nombres = {
#     'magico' : personajes[0],
#     'experto' : personajes[1],
#     'espadachin' : personajes[2]
# }

for key,i in enumerate(personajes): #llave -> valor
    print(key,i) #Evaluación if
    #Buscar la posición de la llave en la lista personajes_value

# print(nombres.values())

# p_magico_dic = nombre["magico"] if p_magico else 

# for i in nombres: 
#     p_magico 
#     if nombres.values() == 1:
#         print(nombres.get('i'))
# elif i == 0:
#     print("Su personaje es")

# for i, j in enumerate(personajes):
#     if j == 1:
#         print(f'Su personaje es: {i}')
#     else:
#         print("Su personaje no cumple con ningun rol")

# print(personajes)
# for i in personajes:
#     if i == 1:
#         print('Su personaje es magico, experto y espadachin')
#     elif i == 0:
#         print('Su personaje no cumple ningún rol')

# if p_magico and p_experto and p_espadachin:
#     print('Su personaje es magico, experto y espadachin')
# elif p_magico and p_experto == 0 and p_espadachin == 0:
#     print("Su personaje es magico")
# elif p_magico and p_experto and p_espadachin == 0:
#     print("Su personaje es magico y experto")
# elif p_magico and p_experto == 0 and p_espadachin:
#     print("Su personaje es magico y espadachin")
# elif p_magico == 0 and p_experto and p_espadachin:
#     print("Su personaje experto y espadachin")
# elif p_magico == 0 and p_experto and p_espadachin == 0:
#     print("Su personaje experto")
# elif p_magico == 0 and p_experto == 0 and p_espadachin:
#     print("Su personaje espadachin")
# elif p_magico == 0 and p_experto == 0 and p_espadachin == 0:
#     print("Su personaje no cumple ningun rol")






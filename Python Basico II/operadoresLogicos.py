
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

for key,i in enumerate(personajes): 
    if i:
        print(f"Su personaje es: {personajes_value[key]}")
    else:
        print(f"Su personaje no es : {personajes_value[key]}")
   



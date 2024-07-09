#Pedir al usuario un usuario y una contraseña y al final mostrar el tamaño de la contraseña 

#Caso prueba
# Ricardo, GatoBonito

# Usuario: Ricardo tu contraseña: ********** y es tamaño: 10
#import getpass

from bullet import Password 

usuario = input("Ingrese su usuario: ")
#contrasenia = getpass.getpass("Ingrese su contraseña: ")
contrasenia = Password("Ingrese su contraseña: ")
p = contrasenia.launch()
#print(type(p))
tamanio = len(p)
print("Tamaño de contraseña: ", tamanio)
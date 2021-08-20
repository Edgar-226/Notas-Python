"""
Proyecto Python y Mysql
-Abrir asistente
-Login o registro
-Si elegimos registro, creara un usuario en la bbdd
-si eloegimos login, identificara  al usuario y nos preguntara 
-Creamos nota, mostrar notas, borrarlas.

"""

from usuarios import acciones

print("""
Acciones disponibles:
    1-registro
    2-login
""")

hazEl = acciones.Acciones()

accion = input("Que quieres hacer?: ")

if accion == "registro" or accion== '1':
   hazEl.registro()

elif accion == "login" or accion == '2':
    hazEl.login()
else:
    print("Haz escogido una opcion invalida adios!!")

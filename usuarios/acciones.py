import usuarios.usuarios as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\nOk !! Vamos a registrarte en el sistema...")
        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("no te has registrado correctamente")
    

    def login(self):
        print("Vale!! Identificate en el sistema...")

        try:
            email = input("Introduce tu email: ")
            clave = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, clave)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el dia {login[5]}")
                self.proximasAcciones(login)
        except:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto intentalo mas tarde")

    def proximasAcciones(self, usuario):
        print("""
        1- Crear nota
        2- Mostrar nota
        3- Eliminar nota
        4- Salir
        """)

        hazEl = notas.acciones.Acciones()

        accion = input("Que quieres Hacer?: ")
        if accion == '1':

            hazEl.crear(usuario)
            self.proximasAcciones(usuario) 
                  
        elif accion == '2':

            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == '3':
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == '4':
            exit() 

        
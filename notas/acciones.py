import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"OK {usuario[1]}!! Vamos a crear una nueva nota...")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Ingresa el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")

        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[3]}")

    def mostrar(self, usuario):
        print(f"Ok {usuario[1]}!! aqui estan tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n***********************************************")
            print(f"Nota:{nota[0]}")
            print(nota[2])
            print(nota[3])
            print("***********************************************")
            

    def borrar(self, usuario):
        print(f"\nOkey {usuario[1]}!! Vamos a borrar la notas")

        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >=1:
            print(f"Hemos borrado la nota {nota.titulo}")
        else:
            print("No se ha podido borrar la nota, intenta despues.....")
import libros
import socios
import prestamos
import reportes

def main():
    while True:
        print("\nSistema de Gestión de Bibliotecas")
        print("1. Gestionar Libros")
        print("2. Gestionar Socios")
        print("3. Gestionar Préstamos y Devoluciones")
        print("4. Generar Reportes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nGestión de Libros")
            print("1. Registrar Libro")
            print("2. Editar Libro")
            print("3. Eliminar Libro")
            print("4. Buscar Libro")
            print("5. Listar Libros")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                editorial = input("Editorial: ")
                año = input("Año de Publicación: ")
                genero = input("Género: ")
                cantidad = int(input("Cantidad Disponible: "))
                libros.agregar_libro(titulo, autor, editorial, año, genero, cantidad)
            elif sub_opcion == "2":
                id_libro = int(input("ID de Libro: "))
                titulo = input("Título: ")
                autor = input("Autor: ")
                editorial = input("Editorial: ")
                año = input("Año de Publicación: ")
                genero = input("Género: ")
                cantidad = int(input("Cantidad Disponible: "))
                libros.editar_libro(id_libro, titulo, autor, editorial, año, genero, cantidad)
            elif sub_opcion == "3":
                id_libro = int(input("ID de Libro: "))
                libros.eliminar_libro(id_libro)
            elif sub_opcion == "4":
                criterio = input("Buscar por (Titulo/Autor/Editorial/Género): ")
                valor = input(f"Ingrese el valor de {criterio}: ")
                resultados = libros.buscar_libro(criterio, valor)
                for libro in resultados:
                    print(libro)
            elif sub_opcion == "5":
                libros_list = libros.listar_libros()
                for libro in libros_list:
                   

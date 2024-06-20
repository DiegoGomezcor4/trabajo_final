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
                    print(libro)

        elif opcion == "2":
            print("\nGestión de Socios")
            print("1. Registrar Socio")
            print("2. Editar Socio")
            print("3. Eliminar Socio")
            print("4. Listar Socios")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                fecha_nacimiento = input("Fecha de Nacimiento: ")
                direccion = input("Dirección: ")
                correo = input("Correo Electrónico: ")
                telefono = input("Teléfono: ")
                socios.agregar_socio(nombre, apellido, fecha_nacimiento, direccion, correo, telefono)
            elif sub_opcion == "2":
                id_socio = int(input("ID de Socio: "))
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                fecha_nacimiento = input("Fecha de Nacimiento: ")
                direccion = input("Dirección: ")
                correo = input("Correo Electrónico: ")
                telefono = input("Teléfono: ")
                socios.editar_socio(id_socio, nombre, apellido, fecha_nacimiento, direccion, correo, telefono)
            elif sub_opcion == "3":
                id_socio = int(input("ID de Socio: "))
                socios.eliminar_socio(id_socio)
            elif sub_opcion == "4":
                socios_list = socios.listar_socios()
                for socio in socios_list:
                    print(socio)

        elif opcion == "3":
            print("\nGestión de Préstamos y Devoluciones")
            print("1. Registrar Préstamo")
            print("2. Registrar Devolución")
            print("3. Listar Préstamos")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                id_socio = int(input("ID de Socio: "))
                id_libro = int(input("ID de Libro: "))
                fecha_prestamo = input("Fecha de Préstamo: ")
                costo = float(input("Costo (0 si no aplica): "))
                prestamos.registrar_prestamo(id_socio, id_libro, fecha_prestamo, costo)
            elif sub_opcion == "2":
                id_prestamo = int(input("ID de Préstamo: "))
                fecha_devolucion = input("Fecha de Devolución: ")
                prestamos.registrar_devolucion(id_prestamo, fecha_devolucion)
            elif sub_opcion == "3":
                prestamos_list = prestamos.listar_prestamos()
                for prestamo in prestamos_list:
                    print(prestamo)

        elif opcion == "4":
            print("\nGenerar Reportes")
            print("1. Reporte por Socio")
            print("2. Reporte por Libro")
            print("3. Reporte por Fecha")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                id_socio = int(input("ID de Socio: "))
                reporte = reportes.reporte_por_socio(id_socio)
                for r in reporte:
                    print(r)
            elif sub_opcion == "2":
                id_libro = int(input("ID de Libro: "))
                reporte = reportes.reporte_por_libro(id_libro)
                for r in reporte:
                    print(r)
            elif sub_opcion == "3":
                fecha_inicio = input("Fecha de Inicio (YYYY-MM-DD): ")
                fecha_fin = input("Fecha de Fin (YYYY-MM-DD): ")
                reporte = reportes.reporte_por_fecha(fecha_inicio, fecha_fin)
                for r in reporte:
                    print(r)

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()

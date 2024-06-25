import libros
import socios
import prestamos
import reportes

def main():
    # MENU PRINCIPAL
    while True:
        print("\nSistema de Gestión de Bibliotecas")
        print("1. Gestionar Libros")
        print("2. Gestionar Socios")
        print("3. Gestionar Préstamos y Devoluciones")
        print("4. Generar Reportes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        # 1 GESTIONAR LIBROS
        if opcion == "1":
            print("Gestión de Libros")
            print("\t 1. Registrar Libro")
            print("\t 2. Editar Libro")
            print("\t 3. Eliminar Libro")
            print("\t 4. Buscar Libro")
            print("\t 5. Listar Libros")
            sub_opcion = input("\t Seleccione una opción: ")

            # 1.1 REGISTRAR LIBRO
            if sub_opcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                editorial = input("Editorial: ")
                año = input("Año de Publicación: ")
                genero = input("Género: ")
                cantidad = int(input("Cantidad Disponible: "))
                libros.agregar_libro(titulo, autor, editorial, año, genero, cantidad)

            # 1.2 EDITAR LIBRO
            elif sub_opcion == "2":
                id_libro = int(input("Ingrese ID del Libro a editar: "))
                titulo = input("Título: ")
                autor = input("Autor: ")
                editorial = input("Editorial: ")
                año = input("Año de Publicación: ")
                genero = input("Género: ")
                cantidad = int(input("Cantidad Disponible: "))
                libros.editar_libro(id_libro, titulo, autor, editorial, año, genero, cantidad)

            # 1.3 ELIMINAR LIBRO
            elif sub_opcion == "3":
                id_libro = int(input("ID de Libro: "))
                libros.eliminar_libro(id_libro)

            # 1.4 BUSCAR LIBRO
            elif sub_opcion == "4":
                print("Busqueda de Libros")
                print("\t\t t. Buscar Libro por titulo")
                print("\t\t a. Buscar Libro por autor")
                print("\t\t e. Buscar Libro por Editorial")
                print("\t\t g. Buscar Libro por genero")
                sub_sub_opcion = input("\t Seleccione una opción: ")
                
                if sub_sub_opcion == "t":
                    criterio = "titulo"
                    valor = input(f"Ingrese el valor de {criterio}: ")
                    resultados = libros.buscar_libro(criterio, valor)
                elif sub_sub_opcion == "a":
                    criterio = "autor"
                    valor = input(f"Ingrese el valor de {criterio}: ")
                    resultados = libros.buscar_libro(criterio, valor)
                elif sub_sub_opcion == "e":
                    criterio = "editorial"
                    valor = input(f"Ingrese el valor de {criterio}: ")
                    resultados = libros.buscar_libro(criterio, valor)
                elif sub_sub_opcion == "g":
                    criterio = "genero"
                    valor = input(f"Ingrese el valor de {criterio}: ")
                    resultados = libros.buscar_libro(criterio, valor)
                    
                for libro in resultados:
                    info_libro = f"""
                        ID del libro: {libro['id_libro']}
                        Título: {libro['titulo']}
                        Autor: {libro['autor']}
                        Editorial: {libro['editorial']}
                        Año de Publicación: {libro['anio_publicacion']}
                        Género: {libro['genero']}
                        Cantidad Disponible: {libro['cantidad_disponible']}
                        """
                    print(info_libro)

            # 1.5 LISTAR LIBROS        
            elif sub_opcion == "5":
                libros.listar_libros()
                
        # 2 GESTIONAR SOCIOS
        elif opcion == "2":
            print("\n \t Gestión de Socios")
            print("\t 1. Registrar Socio")
            print("\t 2. Editar Socio")
            print("\t 3. Eliminar Socio")
            print("\t 4. Listar Socios")
            sub_opcion = input("\t Seleccione una opción: ")

            # 2.1 REGISTRAR SOCIOS
            if sub_opcion == "1":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                fecha_nacimiento = input("Fecha de Nacimiento: ")
                direccion = input("Dirección: ")
                correo = input("Correo Electrónico: ")
                telefono = input("Teléfono: ")
                socios.agregar_socio(nombre, apellido, fecha_nacimiento, direccion, correo, telefono)
            
            # 2.2 EDITAR SOCIO
            elif sub_opcion == "2":
                id_socio = int(input("ID de Socio: "))
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                fecha_nacimiento = input("Fecha de Nacimiento: ")
                direccion = input("Dirección: ")
                correo = input("Correo Electrónico: ")
                telefono = input("Teléfono: ")
                socios.editar_socio(id_socio, nombre, apellido, fecha_nacimiento, direccion, correo, telefono)
            

            # 2.3 ELIMINAR SOCIO
            elif sub_opcion == "3":
                id_socio = int(input("ID de Socio: "))
                socios.eliminar_socio(id_socio)

            # 2.4 LISTAR SOCIOS
            elif sub_opcion == "4":
                socios.listar_socios()
        
        # 3 GESTIONAR PRESTAMOS Y DEVOLUCIONES
        elif opcion == "3":
            print("\n \t Gestión de Préstamos y Devoluciones")
            print("\t 1. Registrar Préstamo")
            print("\t 2. Registrar Devolución")
            print("\t 3. Listar Préstamos")
            sub_opcion = input("\t Seleccione una opción: ")
            # 3.1 REGISTRO PRESTAMO
            if sub_opcion == "1":
                id_socio = int(input("ID de Socio: "))
                id_libro = int(input("ID de Libro: "))
                fecha_prestamo = input("Fecha de Préstamo: ")
                prestamos.registrar_prestamo(id_socio, id_libro, fecha_prestamo)

            # 3.2 REGISTRO DEVOLUCION
            elif sub_opcion == "2":
                id_prestamo = int(input("ID de Préstamo: "))
                fecha_devolucion = input("Fecha de Devolución: ")
                prestamos.registrar_devolucion(id_prestamo, fecha_devolucion)

            # 3.3 LISTAR PRESTAMO
            elif sub_opcion == "3":
                prestamos_list = prestamos.listar_prestamos()
                for prestamo in prestamos_list:
                    print(prestamo)

        # 4. GENERAR REPORTES
        elif opcion == "4":
            print("\n\t Generar Reportes")
            print("\t 1. Reporte por Socio")
            print("\t 2. Reporte por Libro")
            print("\t 3. Reporte por Fecha")
            sub_opcion = input("\t 1Seleccione una opción: ")

            # 4.1 REPORTE POR SOCIO
            if sub_opcion == "1":
                id_socio = int(input("ID de Socio: "))
                reporte = reportes.reporte_por_socio(id_socio)
                for r in reporte:
                    print(r)

            # 4.2 REPORTE POR LIBRO
            elif sub_opcion == "2":
                id_libro = int(input("ID de Libro: "))
                reporte = reportes.reporte_por_libro(id_libro)
                for r in reporte:
                    print(r)

            # 4.3 REPORTE POR FECHA
            elif sub_opcion == "3":
                fecha_inicio = input("Fecha de Inicio (DD-MM-YYYY): ")
                fecha_fin = input("Fecha de Fin (DD-MM-YYYY): ")
                reporte = reportes.reporte_por_fecha(fecha_inicio, fecha_fin)
                for r in reporte:
                    print(r)
                
        # 5 SALIR
        elif opcion == "5":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    main()

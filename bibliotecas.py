
import json
from datetime import datetime

# Funciones para manejar libros
def agregar_libro(libros, titulo, autor, editorial, año_publicacion, genero, cantidad_disponible):
    libro_id = len(libros) + 1
    libro = {
        "ID": libro_id,
        "Título": titulo,
        "Autor": autor,
        "Editorial": editorial,
        "Año de Publicación": año_publicacion,
        "Género": genero,
        "Cantidad Disponible": cantidad_disponible
    }
    libros.append(libro)

def buscar_libro(libros, **kwargs):
    resultados = []
    for libro in libros:
        match = True
        for key, value in kwargs.items():
            if libro.get(key) != value:
                match = False
                break
        if match:
            resultados.append(libro)
    return resultados

# Funciones para manejar socios
def agregar_socio(socios, nombre, apellido, fecha_nacimiento, direccion, email, telefono):
    socio_id = len(socios) + 1
    socio = {
        "ID": socio_id,
        "Nombre": nombre,
        "Apellido": apellido,
        "Fecha de Nacimiento": fecha_nacimiento,
        "Dirección": direccion,
        "Correo Electrónico": email,
        "Teléfono": telefono
    }
    socios.append(socio)

# Funciones para manejar préstamos
def registrar_prestamo(prestamos, id_socio, id_libro, fecha_prestamo, costo=0.0):
    prestamo_id = len(prestamos) + 1
    prestamo = {
        "ID": prestamo_id,
        "ID de Socio": id_socio,
        "ID de Libro": id_libro,
        "Fecha de Préstamo": fecha_prestamo,
        "Costo": costo,
        "Fecha de Devolución": None,
        "Estado": "En Curso"
    }
    prestamos.append(prestamo)
    return prestamo

def devolver_libro(prestamos, id_prestamo):
    for prestamo in prestamos:
        if prestamo["ID"] == id_prestamo:
            prestamo["Fecha de Devolución"] = datetime.now().strftime("%Y-%m-%d")
            prestamo["Estado"] = "Devuelto"
            break

def generar_reporte_prestamos(prestamos, **kwargs):
    resultados = []
    for prestamo in prestamos:
        match = True
        for key, value in kwargs.items():
            if prestamo.get(key) != value:
                match = False
                break
        if match:
            resultados.append(prestamo)
    return resultados

# Funciones para manejar el almacenamiento en JSON
def guardar_datos(libros, socios, prestamos):
    datos = {
        "libros": libros,
        "socios": socios,
        "prestamos": prestamos
    }
    with open("biblioteca.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def cargar_datos():
    try:
        with open("biblioteca.json", "r") as f:
            datos = json.load(f)
            return datos["libros"], datos["socios"], datos["prestamos"]
    except FileNotFoundError:
        return [], [], []

# Función del menú interactivo
def menu():
    libros, socios, prestamos = cargar_datos()
    
    while True:
        print("\n1. Registrar libro")
        print("2. Registrar socio")
        print("3. Registrar préstamo")
        print("4. Registrar devolución")
        print("5. Buscar libro")
        print("6. Generar reporte de préstamos")
        print("7. Guardar y salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            editorial = input("Editorial: ")
            año_publicacion = input("Año de Publicación: ")
            genero = input("Género: ")
            cantidad_disponible = int(input("Cantidad Disponible: "))
            agregar_libro(libros, titulo, autor, editorial, año_publicacion, genero, cantidad_disponible)
        
        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
            direccion = input("Dirección: ")
            email = input("Correo Electrónico: ")
            telefono = input("Teléfono: ")
            agregar_socio(socios, nombre, apellido, fecha_nacimiento, direccion, email, telefono)
        
        elif opcion == "3":
            id_socio = int(input("ID de Socio: "))
            id_libro = int(input("ID de Libro: "))
            fecha_prestamo = input("Fecha de Préstamo (YYYY-MM-DD): ")
            costo = float(input("Costo (0 si no aplica): "))
            prestamo = registrar_prestamo(prestamos, id_socio, id_libro, fecha_prestamo, costo)
            print(f"Préstamo registrado: {prestamo}")
        
        elif opcion == "4":
            id_prestamo = int(input("ID de Préstamo: "))
            devolver_libro(prestamos, id_prestamo)
        
        elif opcion == "5":
            criterios = {}
            titulo = input("Título (dejar vacío si no aplica): ")
            if titulo:
                criterios['Título'] = titulo
            autor = input("Autor (dejar vacío si no aplica): ")
            if autor:
                criterios['Autor'] = autor
            genero = input("Género (dejar vacío si no aplica): ")
            if genero:
                criterios['Género'] = genero
            editorial = input("Editorial (dejar vacío si no aplica): ")
            if editorial:
                criterios['Editorial'] = editorial
            
            resultados = buscar_libro(libros, **criterios)
            for libro in resultados:
                print(libro)
        
        elif opcion == "6":
            criterios = {}
            id_socio = input("ID de Socio (dejar vacío si no aplica): ")
            if id_socio:
                criterios['ID de Socio'] = int(id_socio)
            id_libro = input("ID de Libro (dejar vacío si no aplica): ")
            if id_libro:
                criterios['ID de Libro'] = int(id_libro)
            estado = input("Estado del Préstamo (En Curso/Devuelto, dejar vacío si no aplica): ")
            if estado:
                criterios['Estado'] = estado
            
            resultados = generar_reporte_prestamos(prestamos, **criterios)
            for prestamo in resultados:
                print(prestamo)
        
        elif opcion == "7":
            guardar_datos(libros, socios, prestamos)
            break

if __name__ == "__main__":
    menu()

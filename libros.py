import json
import os

LIBROS_FILE = 'libros.json'
LAST_ID_FILE = 'last_id_libro.txt'

# Funciones para generar un id unico:
def cargar_ultimo_id():
    try:
        with open(LAST_ID_FILE, 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0  # Si el archivo no existe, asumimos que el último ID es 0

def guardar_ultimo_id(ultimo_id):
    with open(LAST_ID_FILE, 'w') as f:
        f.write(str(ultimo_id))

def generar_nuevo_id():
    ultimo_id = cargar_ultimo_id()
    nuevo_id = ultimo_id + 1
    guardar_ultimo_id(nuevo_id)
    return nuevo_id


# funciones de libros:
def cargar_libros():
    if os.path.exists(LIBROS_FILE):
        with open(LIBROS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_libros(libros):
    with open(LIBROS_FILE, 'w', encoding='utf-8') as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)
        
def agregar_libro(titulo, autor, editorial, año, genero, cantidad):
    libros = cargar_libros()
    nuevo_id = generar_nuevo_id()
    nuevo_libro = {
        "id_libro": nuevo_id,
        "titulo": titulo,
        "autor": autor,
        "editorial": editorial,
        "anio_publicacion": año,
        "genero": genero,
        "cantidad_disponible": cantidad
    }
    libros.append(nuevo_libro)
    print(f'\n \t MENSAJE: El libro {titulo}, fue agregado con el id: {nuevo_id}')
    guardar_libros(libros)

def editar_libro(id_libro, titulo, autor, editorial, año, genero, cantidad):
    libros = cargar_libros()
    for libro in libros:
        if libro["id_libro"] == id_libro:
            libro.update({
                "titulo": titulo,
                "autor": autor,
                "editorial": editorial,
                "anio_publicacion": año,
                "genero": genero,
                "cantidad_disponible": cantidad
            })
            guardar_libros(libros)
            print(f'\n \t MENSAJE: el libro: {titulo} fue editado correctamente')
            return

def eliminar_libro(id_libro):
    libros = cargar_libros()
    
    #se genera una nueva lista sin el libro eliminado
    nueva_lista_libros = []
    for libro in libros:
        if libro["id_libro"] != id_libro:
            nueva_lista_libros.append(libro)
    libros = nueva_lista_libros
    
    guardar_libros(libros)

def buscar_libro(criterio, valor):
    libros = cargar_libros()
    resultados = []
    for libro in libros:
        if libro[criterio] == valor:
            resultados.append(libro)
    return resultados

def listar_libros():
    
    libros_list = cargar_libros()
    print("\n \t LISTADO DE LIBROS: ")
    for libro in libros_list:
        print(f"\n \t ID Libro: {libro['id_libro']}")
        print(f"\t Título: {libro['titulo']}")
        print(f"\t Autor: {libro['autor']}")
        print(f"\t Editorial: {libro['editorial']}")
        print(f"\t Año de Publicación: {libro['anio_publicacion']}")
        print(f"\t Género: {libro['genero']}")
        print(f"\t Cantidad Disponible: {libro['cantidad_disponible']}")
        print("\t " + "-" * 20)


def prestar_libro(id_libro):
    libros = cargar_libros()
    for libro in libros:
        if libro["id_libro"] == id_libro:
            if libro["cantidad_disponible"] > 0:
                libro["cantidad_disponible"] -= 1
                guardar_libros(libros)
                print(f"\n \t MENSAJE: Se ha prestado el libro '{libro['titulo']}'. Quedan {libro['cantidad_disponible']} copias disponibles.")
                return True
            else:
                print(f"\n \t MENSAJE: No hay copias disponibles del libro '{libro['titulo']}'.")
                return False
    print(f"\n \t MENSAJE: No se encontró el libro con ID {id_libro}.")
    
def devolver_libro(id_libro):
    libros = cargar_libros()
    for libro in libros:
        if libro["id_libro"] == id_libro:
            libro["cantidad_disponible"] += 1
            guardar_libros(libros)
            print(f"\n \t MENSAJE: Se ha devuelto el libro '{libro['titulo']}'. Ahora hay {libro['cantidad_disponible']} copias disponibles.")
            return
    print(f"\n \t MENSAJE: No se encontró el libro con ID {id_libro}.")
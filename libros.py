import json
import os

LIBROS_FILE = 'libros.json'

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
    id_libro = len(libros) + 1
    nuevo_libro = {
        "id_libro": id_libro,
        "titulo": titulo,
        "autor": autor,
        "editorial": editorial,
        "anio_publicacion": año,
        "genero": genero,
        "cantidad_disponible": cantidad
    }
    libros.append(nuevo_libro)
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
            return

def eliminar_libro(id_libro):
    libros = cargar_libros()
    libros = [libro for libro in libros if libro["id_libro"] != id_libro]
    guardar_libros(libros)

def buscar_libro(criterio, valor):
    libros = cargar_libros()
    resultados = [libro for libro in libros if libro[criterio] == valor]
    return resultados

def listar_libros():
    return cargar_libros()

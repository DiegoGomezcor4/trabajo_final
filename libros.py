import json
import os

LIBROS_FILE = 'libros.json'

def cargar_libros():
    if os.path.exists(LIBROS_FILE):
        with open(LIBROS_FILE, 'r') as f:
            return json.load(f)
    return []

def guardar_libros(libros):
    with open(LIBROS_FILE, 'w') as f:
        json.dump(libros, f, indent=4)

def agregar_libro(titulo, autor, editorial, año, genero, cantidad):
    libros = cargar_libros()
    id_libro = len(libros) + 1
    nuevo_libro = {
        "ID": id_libro,
        "Titulo": titulo,
        "Autor": autor,
        "Editorial": editorial,
        "Año": año,
        "Genero": genero,
        "Cantidad": cantidad
    }
    libros.append(nuevo_libro)
    guardar_libros(libros)

def editar_libro(id_libro, titulo, autor, editorial, año, genero, cantidad):
    libros = cargar_libros()
    for libro in libros:
        if libro["ID"] == id_libro:
            libro.update({
                "Titulo": titulo,
                "Autor": autor,
                "Editorial": editorial,
                "Año": año,
                "Genero": genero,
                "Cantidad": cantidad
            })
            guardar_libros(libros)
            return

def eliminar_libro(id_libro):
    libros = cargar_libros()
    libros = [libro for libro in libros if libro["ID"] != id_libro]
    guardar_libros(libros)

def buscar_libro(criterio, valor):
    libros = cargar_libros()
    resultados = [libro for libro in libros if libro[criterio] == valor]
    return resultados

def listar_libros():
    return cargar_libros()

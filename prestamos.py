import json
import os
import libros
from datetime import datetime

PRESTAMOS_FILE = 'prestamos.json'

def cargar_prestamos():
    if os.path.exists(PRESTAMOS_FILE):
        with open(PRESTAMOS_FILE, 'r') as f:
            return json.load(f)
    return []

def guardar_prestamos(prestamos):
    with open(PRESTAMOS_FILE, 'w') as f:
        json.dump(prestamos, f, indent=4)

def registrar_prestamo(id_socio, id_libro, fecha_prestamo):
    prestamos = cargar_prestamos()
    id_prestamo = len(prestamos) + 1
    nuevo_prestamo = {
        "id_prestamo": id_prestamo,
        "id_socio": id_socio,
        "id_libro": id_libro,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": None,
        "estado": "En Curso"
    }
    
    if libros.prestar_libro(id_libro):
        prestamos.append(nuevo_prestamo)
        guardar_prestamos(prestamos)
    
    
    
    

def registrar_devolucion(id_prestamo, fecha_devolucion):
    prestamos = cargar_prestamos()
    for prestamo in prestamos:
        if prestamo["id_prestamo"] == id_prestamo and prestamo["estado"] == "En Curso":
            prestamo.update({
                "fecha_devolucion": fecha_devolucion,
                "estado": "Devuelto"
            })
            print(f'MENSAJE: el prestamo {id_prestamo} ha sido devuelto')
            guardar_prestamos(prestamos)
            libros.devolver_libro(prestamo["id_libro"])
            return
        elif prestamo["id_prestamo"] == id_prestamo and prestamo["estado"] == "Devuelto":
            print("El prestamo que intenta devolver ya ha sido devuelto!")
            
            


def listar_prestamos():
    return cargar_prestamos()

def prestamos_por_socio(id_socio):
    prestamos = cargar_prestamos()
    return [prestamo for prestamo in prestamos if prestamo["id_socio"] == id_socio]

def prestamos_por_libro(id_libro):
    prestamos = cargar_prestamos()
    return [prestamo for prestamo in prestamos if prestamo["id_libro"] == id_libro]

def prestamos_por_fecha(fecha_inicio, fecha_fin):
    prestamos = cargar_prestamos()
    fecha_inicio = datetime.strptime(fecha_inicio, '%d-%m-%Y')
    fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%Y')
    return [
        prestamo for prestamo in prestamos
        if fecha_inicio <= datetime.strptime(prestamo["fecha_prestamo"], '%d-%m-%Y') <= fecha_fin
    ]

import json
import os
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

def registrar_prestamo(id_socio, id_libro, fecha_prestamo, costo=0.0):
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
            guardar_prestamos(prestamos)
            return

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
    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
    return [
        prestamo for prestamo in prestamos
        if fecha_inicio <= datetime.strptime(prestamo["fecha_prestamo"], '%Y-%m-%d') <= fecha_fin
    ]

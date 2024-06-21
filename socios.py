import json
import os
import pandas as pd

SOCIOS_FILE = 'socios.json'

def cargar_socios():
    if os.path.exists(SOCIOS_FILE):
        with open(SOCIOS_FILE, 'r') as f:
            return json.load(f)
    return []

def guardar_socios(socios):
    with open(SOCIOS_FILE, 'w') as f:
        json.dump(socios, f, indent=4)

def agregar_socio(nombre, apellido, fecha_nacimiento, direccion, correo, telefono):
    socios = cargar_socios()
    id_socio = len(socios) + 1
    nuevo_socio = {
        "id_socio": id_socio,
        "nombre": nombre,
        "apellido": apellido,
        "fecha_nacimiento": fecha_nacimiento,
        "direccion": direccion,
        "correo_electronico": correo,
        "telefono": telefono
    }
    socios.append(nuevo_socio)
    guardar_socios(socios)

def editar_socio(id_socio, nombre, apellido, fecha_nacimiento, direccion, correo, telefono):
    socios = cargar_socios()
    for socio in socios:
        if socio["id_socio"] == id_socio:
            socio.update({
                "nombre": nombre,
                "apellido": apellido,
                "fecha_nacimiento": fecha_nacimiento,
                "direccion": direccion,
                "correo_electronico": correo,
                "telefono": telefono
            })
            guardar_socios(socios)
            return

def eliminar_socio(id_socio):
    socios = cargar_socios()
    socios = [socio for socio in socios if socio["id_socio"] != id_socio]
    guardar_socios(socios)

def listar_socios():
    socios_list = cargar_socios()
                
    # agregar tabla
    # Crear un DataFrame de pandas
    df = pd.DataFrame(socios_list)

    # Mostrar la tabla
    print('\n',df)

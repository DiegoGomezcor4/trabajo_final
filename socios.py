import json
import os

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
        "ID": id_socio,
        "Nombre": nombre,
        "Apellido": apellido,
        "FechaNacimiento": fecha_nacimiento,
        "Direccion": direccion,
        "Correo": correo,
        "Telefono": telefono
    }
    socios.append(nuevo_socio)
    guardar_socios(socios)

def editar_socio(id_socio, nombre, apellido, fecha_nacimiento, direccion, correo, telefono):
    socios = cargar_socios()
    for socio in socios:
        if socio["ID"] == id_socio:
            socio.update({
                "Nombre": nombre,
                "Apellido": apellido,
                "FechaNacimiento": fecha_nacimiento,
                "Direccion": direccion,
                "Correo": correo,
                "Telefono": telefono
            })
            guardar_socios(socios)
            return

def eliminar_socio(id_socio):
    socios = cargar_socios()
    socios = [socio for socio in socios if socio["ID"] != id_socio]
    guardar_socios(socios)

def listar_socios():
    return cargar_socios()

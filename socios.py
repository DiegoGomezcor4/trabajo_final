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
    
    for socio in socios_list:
        print(f"ID Socio: {socio['id_socio']}")
        print(f"Nombre: {socio['nombre']}")
        print(f"Apellido: {socio['apellido']}")
        print(f"Fecha de Nacimiento: {socio['fecha_nacimiento']}")
        print(f"Dirección: {socio['direccion']}")
        print(f"Correo Electrónico: {socio['correo_electronico']}")
        print(f"Teléfono: {socio['telefono']}")
        print("-" * 20)

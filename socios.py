import json
import os

SOCIOS_FILE = 'socios.json'
LAST_ID_FILE = 'last_id_socios.txt'

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

# funciones de los socios
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
    nuevo_id = generar_nuevo_id()
    nuevo_socio = {
        "id_socio": nuevo_id,
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
    
    #se genera una nueva lista sin el libro eliminado
    nueva_lista_socios = []
    for socio in socios:
        if socio["id_socio"] != id_socio:
            nueva_lista_socios.append(socio)
    socios = nueva_lista_socios
    
    guardar_socios(socios)

def listar_socios():
    socios_list = cargar_socios()
    print("\n \t LISTADO DE SOCIOS: ")
    for socio in socios_list:
        print(f"\n \tID Socio: {socio['id_socio']}")
        print(f"\tNombre: {socio['nombre']}")
        print(f"\tApellido: {socio['apellido']}")
        print(f"\tFecha de Nacimiento: {socio['fecha_nacimiento']}")
        print(f"\tDirección: {socio['direccion']}")
        print(f"\tCorreo Electrónico: {socio['correo_electronico']}")
        print(f"\tTeléfono: {socio['telefono']}")
        print("\t" + "-" * 20)

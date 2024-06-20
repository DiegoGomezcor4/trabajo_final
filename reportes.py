from prestamos import listar_prestamos, prestamos_por_socio, prestamos_por_libro, prestamos_por_fecha

def reporte_por_socio(id_socio):
    return prestamos_por_socio(id_socio)

def reporte_por_libro(id_libro):
    return prestamos_por_libro(id_libro)

def reporte_por_fecha(fecha_inicio, fecha_fin):
    return prestamos_por_fecha(fecha_inicio, fecha_fin)

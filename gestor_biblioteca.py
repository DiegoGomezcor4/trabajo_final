import tkinter as tk
from tkinter import messagebox
import libros
import socios
import prestamos
import reportes

# Funciones para las acciones del menú principal
def gestionar_libros():
    ventana_libros = tk.Toplevel(root)
    ventana_libros.title("Gestión de Libros")
    
    # Agregar widgets para gestionar libros
    tk.Label(ventana_libros, text="Título:").grid(row=0, column=0, padx=10, pady=10)
    entry_titulo = tk.Entry(ventana_libros)
    entry_titulo.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(ventana_libros, text="Autor:").grid(row=1, column=0, padx=10, pady=10)
    entry_autor = tk.Entry(ventana_libros)
    entry_autor.grid(row=1, column=1, padx=10, pady=10)
    
    tk.Label(ventana_libros, text="Editorial:").grid(row=2, column=0, padx=10, pady=10)
    entry_editorial = tk.Entry(ventana_libros)
    entry_editorial.grid(row=2, column=1, padx=10, pady=10)
    
    tk.Label(ventana_libros, text="Año de Publicación:").grid(row=3, column=0, padx=10, pady=10)
    entry_anio = tk.Entry(ventana_libros)
    entry_anio.grid(row=3, column=1, padx=10, pady=10)
    
    tk.Label(ventana_libros, text="Género:").grid(row=4, column=0, padx=10, pady=10)
    entry_genero = tk.Entry(ventana_libros)
    entry_genero.grid(row=4, column=1, padx=10, pady=10)
    
    tk.Label(ventana_libros, text="Cantidad Disponible:").grid(row=5, column=0, padx=10, pady=10)
    entry_cantidad = tk.Entry(ventana_libros)
    entry_cantidad.grid(row=5, column=1, padx=10, pady=10)
    
    def agregar_libro():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        editorial = entry_editorial.get()
        anio = entry_anio.get()
        genero = entry_genero.get()
        cantidad = int(entry_cantidad.get())
        libros.agregar_libro(titulo, autor, editorial, anio, genero, cantidad)
        messagebox.showinfo("Éxito", "Libro agregado correctamente")
    
    tk.Button(ventana_libros, text="Agregar Libro", command=agregar_libro).grid(row=6, column=0, columnspan=2, pady=10)
    
    # Puedes añadir más botones y funcionalidades para editar, eliminar, buscar y listar libros aquí

def gestionar_socios():
    ventana_socios = tk.Toplevel(root)
    ventana_socios.title("Gestión de Socios")
    
    # Agregar widgets para gestionar socios
    tk.Label(ventana_socios, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
    entry_nombre = tk.Entry(ventana_socios)
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(ventana_socios, text="Apellido:").grid(row=1, column=0, padx=10, pady=10)
    entry_apellido = tk.Entry(ventana_socios)
    entry_apellido.grid(row=1, column=1, padx=10, pady=10)
    
    tk.Label(ventana_socios, text="Fecha de Nacimiento:").grid(row=2, column=0, padx=10, pady=10)
    entry_fecha_nacimiento = tk.Entry(ventana_socios)
    entry_fecha_nacimiento.grid(row=2, column=1, padx=10, pady=10)
    
    tk.Label(ventana_socios, text="Dirección:").grid(row=3, column=0, padx=10, pady=10)
    entry_direccion = tk.Entry(ventana_socios)
    entry_direccion.grid(row=3, column=1, padx=10, pady=10)
    
    tk.Label(ventana_socios, text="Correo Electrónico:").grid(row=4, column=0, padx=10, pady=10)
    entry_correo = tk.Entry(ventana_socios)
    entry_correo.grid(row=4, column=1, padx=10, pady=10)
    
    tk.Label(ventana_socios, text="Teléfono:").grid(row=5, column=0, padx=10, pady=10)
    entry_telefono = tk.Entry(ventana_socios)
    entry_telefono.grid(row=5, column=1, padx=10, pady=10)
    
    def agregar_socio():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        fecha_nacimiento = entry_fecha_nacimiento.get()
        direccion = entry_direccion.get()
        correo = entry_correo.get()
        telefono = entry_telefono.get()
        socios.agregar_socio(nombre, apellido, fecha_nacimiento, direccion, correo, telefono)
        messagebox.showinfo("Éxito", "Socio agregado correctamente")
    
    tk.Button(ventana_socios, text="Agregar Socio", command=agregar_socio).grid(row=6, column=0, columnspan=2, pady=10)
    
    # Puedes añadir más botones y funcionalidades para editar, eliminar y listar socios aquí

def gestionar_prestamos():
    ventana_prestamos = tk.Toplevel(root)
    ventana_prestamos.title("Gestión de Préstamos y Devoluciones")
    
    # Agregar widgets para gestionar préstamos y devoluciones
    tk.Label(ventana_prestamos, text="ID de Socio:").grid(row=0, column=0, padx=10, pady=10)
    entry_id_socio = tk.Entry(ventana_prestamos)
    entry_id_socio.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(ventana_prestamos, text="ID de Libro:").grid(row=1, column=0, padx=10, pady=10)
    entry_id_libro = tk.Entry(ventana_prestamos)
    entry_id_libro.grid(row=1, column=1, padx=10, pady=10)
    
    tk.Label(ventana_prestamos, text="Fecha de Préstamo:").grid(row=2, column=0, padx=10, pady=10)
    entry_fecha_prestamo = tk.Entry(ventana_prestamos)
    entry_fecha_prestamo.grid(row=2, column=1, padx=10, pady=10)
    
    tk.Label(ventana_prestamos, text="Costo:").grid(row=3, column=0, padx=10, pady=10)
    entry_costo = tk.Entry(ventana_prestamos)
    entry_costo.grid(row=3, column=1, padx=10, pady=10)
    
    def registrar_prestamo():
        id_socio = int(entry_id_socio.get())
        id_libro = int(entry_id_libro.get())
        fecha_prestamo = entry_fecha_prestamo.get()
        costo = float(entry_costo.get())
        prestamos.registrar_prestamo(id_socio, id_libro, fecha_prestamo, costo)
        messagebox.showinfo("Éxito", "Préstamo registrado correctamente")
    
    tk.Button(ventana_prestamos, text="Registrar Préstamo", command=registrar_prestamo).grid(row=4, column=0, columnspan=2, pady=10)
    
    # Puedes añadir más botones y funcionalidades para registrar devoluciones y listar préstamos aquí

def generar_reportes():
    ventana_reportes = tk.Toplevel(root)
    ventana_reportes.title("Generar Reportes")
    
    # Agregar widgets para generar reportes
    tk.Label(ventana_reportes, text="ID de Socio:").grid(row=0, column=0, padx=10, pady=10)
    entry_id_socio = tk.Entry(ventana_reportes)
    entry_id_socio.grid(row=0, column=1, padx=10, pady=10)
    
    def reporte_por_socio():
        id_socio = int(entry_id_socio.get())
        reporte = reportes.reporte_por_socio(id_socio)
        ventana_reporte = tk.Toplevel(ventana_reportes)
        ventana_reporte.title("Reporte")
        tk.Text(ventana_reporte, wrap=tk.WORD, height=20, width=50).pack(padx=10, pady=10)
        tk.Label(ventana_reporte, text=reporte).pack(padx=10, pady=10)
    
    tk.Button(ventana_reportes, text="Generar Reporte", command=reporte_por_socio).grid(row=1, column=0, columnspan=2, pady=10)
    
    # Puedes añadir más botones y funcionalidades para generar otros tipos de reportes aquí

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Biblioteca")

# Botones del menú principal
tk.Button(root, text="Gestión de Libros", command=gestionar_libros).pack(pady=10)
tk.Button(root, text="Gestión de Socios", command=gestionar_socios).pack(pady=10)
tk.Button(root, text="Gestión de Préstamos y Devoluciones", command=gestionar_prestamos).pack(pady=10)
tk.Button(root, text="Generar Reportes", command=generar_reportes).pack(pady=10)

root.mainloop()

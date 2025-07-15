import os

# --- Datos de Proyectos (Puedes modificar y añadir más aquí) ---
# Esta es una lista de diccionarios, donde cada diccionario representa un proyecto.
# Puedes añadir más campos como 'fecha_inicio', 'fecha_fin', 'responsable', etc.
proyectos_ejemplo = [
    {"nombre": "Desarrollo App Móvil", "descripcion": "Creación de una aplicación para gestión de tareas.", "estado": "En progreso"},
    {"nombre": "Diseño Web Corporativo", "descripcion": "Rediseño completo de la página web de la empresa.", "estado": "Pendiente"},
    {"nombre": "Auditoría de Seguridad", "descripcion": "Revisión exhaustiva de los sistemas de seguridad.", "estado": "Completado"},
    {"nombre": "Migración a la Nube", "descripcion": "Traslado de infraestructura de servidores a AWS.", "estado": "En progreso"}
]

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo de script Python.
    :param ruta_script: La ruta (absoluta o relativa) al archivo del script.
    """
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            # Asegura encoding UTF-8
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
            print(archivo.read())
            print(f"\n--- Fin del Código de {os.path.basename(ruta_script)} ---\n")
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_script_absoluta}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def listar_proyectos(proyectos_data):
    """
    Muestra una lista detallada de los proyectos.
    :param proyectos_data: Una lista de diccionarios con la información de los proyectos.
    """
    print("\n--- Lista de Proyectos ---")
    if not proyectos_data:
        print("No hay proyectos registrados en este momento.")
        print("--------------------------")
        return
    for i, proyecto in enumerate(proyectos_data):
        print(f"\nProyecto {i+1}:")
        print(f"  Nombre: {proyecto.get('nombre', 'N/A')}")
        print(f"  Descripción: {proyecto.get('descripcion', 'N/A')}")
        print(f"  Estado: {proyecto.get('estado', 'N/A')}")
        # Puedes añadir más detalles aquí si agregas más campos a tus proyectos_ejemplo
    print("\n--------------------------")

def mostrar_menu():
    """
    Muestra el menú principal del Dashboard y gestiona las opciones del usuario.
    """
    # Define la ruta base donde se encuentra el dashboard.py
    # os.path.dirname(__file__) obtiene el directorio del script actual.
    ruta_base = os.path.dirname(__file__)

    # Diccionario de opciones del menú
    # 'clave': 'ruta/al/script.py' para mostrar código
    # 'clave': 'función_a_llamar' para funcionalidades internas
    opciones = {
        '1': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'listar_proyectos'  # Nueva opción para listar proyectos
        # Agrega aquí el resto de las rutas de los scripts o nombres de funciones
        # Ejemplo: '3': 'ruta/a/otro_script.py',
        # Ejemplo: '4': 'otra_funcion_interna'
    }

    while True:
        print("\n--- Menu Principal - Dashboard de Gestión de Proyectos ---")
        # Imprime las opciones del menú
        for key, value in opciones.items():
            if value == 'listar_proyectos':  # Si es la opción de proyectos
                print(f"{key} - Listar Proyectos")
            elif isinstance(value, str) and value.endswith('.py'):  # Si es un script
                # Extrae solo el nombre del script para mostrarlo en el menú
                script_name = os.path.basename(value)
                print(f"{key} - Mostrar Código de {script_name}")
            else:  # Para futuras funciones internas
                print(f"{key} - {value.replace('_', ' ').title()}")  # Formateo básico
        print("0 - Salir")

        eleccion = input("Elige una opción ('0' para salir): ")

        if eleccion == '0':
            print("Saliendo del Dashboard. ¡Hasta pronto!")
            break
        elif eleccion in opciones:
            accion = opciones[eleccion]
            if accion == 'listar_proyectos':
                listar_proyectos(proyectos_ejemplo)  # Llama a la función de listar proyectos
            elif isinstance(accion, str) and accion.endswith('.py'):
                # Asegura que el path sea absoluto
                ruta_script = os.path.join(ruta_base, accion)
                mostrar_codigo(ruta_script)
            else:
                # Aquí puedes añadir lógica para otras funciones internas
                print(f"La funcionalidad '{accion}' aún no está implementada.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo con un número del menú.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()

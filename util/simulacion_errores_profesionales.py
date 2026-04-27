import random
from datetime import datetime, timedelta

def generar_simulacion_errores_profesional(numeroProfesionales):

    nombres = ["Esteban", "Maria", "Juan", "Ana", "Luis"]
    apellidos = ["Vaneas", "Gonzalez", "Perez", "Rodriguez", "Lopez"]
    correos = ["esteban@gmail.com", "maria@gmail.com", "juan@gmail.com", "ana@gmail.com", "luis@gmail.com"]
    contraseñas = ["1234", "5678", "abcd", "efgh", "ijkl"]
    telefonos = ["3101234567", "3109876543", "3105555555", "3101111111", "3102222222"]
    profesiones = ["Abogado", "Medico", "Ingeniero", "Arquitecto", "Profesor"]

    # Fecha base para generar fechas aleatorias
    fechaInicio = datetime(2020, 1, 1)

    # Lista donde se guardan todas las simulaciones
    simulaciones = []

    for _ in range(numeroProfesionales):

        # Registro válido para datos limpios
        simulacion = {
            "id_profesional": random.randint(1, 400),
            "id_usuaria": random.randint(1, 400),
            "nombre": random.choice(nombres),
            "apellido": random.choice(apellidos),
            "email": random.choice(correos),
            "contraseña": random.choice(contraseñas),
            "telefono": random.choice(telefonos),
            "profesion": random.choice(profesiones),
            "fecha": fechaInicio + timedelta(days=random.randint(0, 2000)),
            "id_cliente": random.randint(1, 400)
        }

        # Se genera una probabilidad entre 0 y 1
        probabilidadError = random.random()

        if probabilidadError < 0.1:
            # Email con formato inválido
            simulacion["email"] = random.choice([
                simulacion["email"].replace("@", ""),    # Elimina el @
                simulacion["email"] + " ",               # Espacio al final
                simulacion["email"].replace(".com", "")  # Quita el dominio
            ])

        elif probabilidadError < 0.2:
            # Teléfono con formato inválido
            simulacion["telefono"] = random.choice([
                simulacion["telefono"][:-2],    # Número incompleto (-2 dígitos)
                " " + simulacion["telefono"],   # Espacio al inicio
                simulacion["telefono"] + "99"   # Número más largo de lo debido
            ])

        elif probabilidadError < 0.3:
            # IDs con valores no válidos
            simulacion["id_profesional"] = random.choice([-1, -10, 0])
            simulacion["id_cliente"] = random.choice([-1, -10, 0])

        elif probabilidadError < 0.4:
            # Fecha con formato incorrecto
            simulacion["fecha"] = simulacion["fecha"].strftime("%d/%m")  # Falta el año

        elif probabilidadError < 0.5:
            # Profesión con problemas de estandarización
            simulacion["profesion"] = random.choice([
                simulacion["profesion"].lower(),   # minúscula
                simulacion["profesion"].upper(),   # mayúscula
                simulacion["profesion"] + " ",     # espacio al final
                " " + simulacion["profesion"]      # espacio al inicio
            ])

        elif probabilidadError < 0.6:
            # Nombre con problemas de estandarización
            simulacion["nombre"] = random.choice([
                simulacion["nombre"].lower(),   # minúscula
                simulacion["nombre"].upper(),   # mayúscula
                " " + simulacion["nombre"],     # espacio al inicio
                simulacion["nombre"] + " "      # espacio al final
            ])

        elif probabilidadError < 0.7:
            # Apellido incompleto, con espacio o vacío
            simulacion["apellido"] = random.choice([
                simulacion["apellido"][:3],    # Apellido recortado
                simulacion["apellido"] + " ",  # Espacio al final
                ""                             # Apellido vacío
            ])

        elif probabilidadError < 0.8:
            # Fecha fuera de rango lógico
            simulacion["fecha"] = random.choice([
                datetime(2030, 1, 1),  # Fecha futura
                datetime(1978, 1, 1)   # Fecha muy antigua
            ])

        elif probabilidadError < 0.9:
            # id_usuaria con valor no válido
            simulacion["id_usuaria"] = random.choice([-1, 0, -99])

        # Acá guardo la simulación (con o sin error)
        simulaciones.append(simulacion)

    # Agrega un duplicado al final
    if len(simulaciones) >= 2:
        simulaciones.append(simulaciones[0].copy())

    return simulaciones
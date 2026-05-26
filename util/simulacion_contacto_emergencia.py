import random

def generar_simulacion_contacto(cantidad):

    nombres = [
        "Carlos", "Maria", "Ana", "Luis",
        "Jorge", "Camila", "Laura", "David"
    ]

    relaciones = [
        "Madre",
        "Padre",
        "Hermano",
        "Amigo",
        "Pareja"
    ]

    contactos = []

    for i in range(cantidad):

        contacto = {
            "nombre": random.choice(nombres),
            "telefono": f"3{random.randint(100000000, 999999999)}",
            "relacion": random.choice(relaciones)
        }

        contactos.append(contacto)

    return contactos
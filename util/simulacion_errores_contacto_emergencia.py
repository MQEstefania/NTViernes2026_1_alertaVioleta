import random

def generar_errores_contacto(contactos):

    contactos_error = []

    for contacto in contactos:

        nuevo_contacto = contacto.copy()

        error = random.choice([
            "telefono",
            "nombre",
            "relacion"
        ])

        if error == "telefono":
            nuevo_contacto["telefono"] = "ERROR"

        elif error == "nombre":
            nuevo_contacto["nombre"] = ""

        elif error == "relacion":
            nuevo_contacto["relacion"] = None

        contactos_error.append(nuevo_contacto)

    return contactos_error
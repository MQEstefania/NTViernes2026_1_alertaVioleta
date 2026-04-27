import random


def generar_codigo(numeroProfesionales):
    nombre = ["Esteban", "Maria", "Juan", "Ana", "Luis"]
    apellido = ["vaneas", "Gonzalez", "Perez", "Rodriguez", "Lopez"]
    email = ["karla@gmail.com", "maria@gmail.com", "juan@gmail.com", "ana@gmail.com", "luis@gmail.com"]
    contraseña = ["1234", "5678", "abcd", "efgh", "ijkl"]
    telefono = ["3101234567", "3109876543", "3105555555", "3101111111", "3102222222"]
    profesion = ["Abogado", "Medico", "Ingeniero", "Arquitecto", "Profesor"]

    servicios = []
    for i in range(numeroProfesionales):
        servicios = {
            "id_profesional": random.randint(0, 400),
            "id_usuaria": random.randint(0, 400),
            "nombre": random.choice(nombre),
            "apellido": random.choice(apellido),
            "email": random.choice(email),
            "contraseña": random.choice(contraseña),
            "telefono": random.choice(telefono),
            "profesion": random.choice(profesion),
            "fecha": fecha.strftime("%Y/%m/%d"),
            "id_cliente": random.randint(0, 400)
        }
        servicios.append(servicios)
    return servicios
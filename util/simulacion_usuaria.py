#Simulando datos de una tabla en Python
import random
from datetime import datetime, timedelta

def generar_usuaria(numeroUsuaria):

    listaNombres=["Ana","Maria","Juliana","Melisa","Sofia"]
    listaApellidos=["Molina","Garcia", "Lopez", "Rodriguez", "Perez"]
    listaEmail=["ana@gmail.com","maria@gmail.com", "juliana@gmail.com", "melisa@gmail.com", "sofia@gmail.com"]
    listaFechaNacimiento= ["1990-01-01","1992-05-15","1988-10-30","1995-07-20","1993-03-12"]
    listaContraseñas=["password123","qwerty456","abcde789","12345abc","passw0rd"]
    listaTelefonos=["1234567890","0987654321","5555555555","1111111111","2222222222"]
    listaUbicaciones=["Ciudad A","Ciudad B","Ciudad C","Ciudad D","Ciudad E"]
    listaFechaRegistro=["2020-01-01","2021-05-15","2019-10-30","2022-07-20","2023-03-12"]   

    fechaInicio=datetime(2026,1,1)
    
    usuarias=[]
    for _ in range (numeroUsuaria):

        fecha=fechaInicio+timedelta(days=random.randint(0,60))

        usuaria={
            "id": random.randint(0,6000),
            "nombre": random.choice(listaNombres),
            "apellido": random.choice(listaApellidos),
            "email": random.choice(listaEmail),
            "fecha_nacimiento": random.choice(listaFechaNacimiento),
            "contraseña": random.choice(listaContraseñas),
            "telefono": random.choice(listaTelefonos),
            "ubicacion": random.choice(listaUbicaciones),
            "fecha_registro": random.choice(listaFechaRegistro),
            "fecha":fecha.strftime("%Y-%m-%d")
        }
        usuarias.append(usuaria)
    return usuarias
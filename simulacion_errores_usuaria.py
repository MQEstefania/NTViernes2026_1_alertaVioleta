import random

from datetime import datetime, timedelta

def generar_simulacion_errores_usuaria(numeroSimulaciones):

    nombres=["Ana","Maria","Juliana","Melisa","Sofia"]
    apellidos=["Molina","Garcia","Lopez","Rodriguez","Perez"]
    correos=["ana@gmail.com","maria@gmail.com","juliana@gmail.com","melisa@gmail.com","sofia@gmail.com"]
    telefonos=["3001234567","3109876543","3205555555","3011111111","3022222222"]
    ubicaciones=["Bogotá","Medellín","Cali","Barranquilla","Cartagena"]
    contraseñas=["password123","qwerty456","abcde789","12345abc","passw0rd"]

    #Fecha base para generar fechas aleatorias
    fechaInicio = datetime(2020,1,1)

    #Lista donde se guardan todas las simulaciones
    simulaciones=[]

    for _ in range(numeroSimulaciones):

        #Registro válido para datos limpios
        simulacion={
            "id": random.randint(1,6000), 
            "nombre": random.choice(nombres),  
            "apellido": random.choice(apellidos),  
            "email": random.choice(correos), 
            "telefono": random.choice(telefonos), 
            "ubicacion": random.choice(ubicaciones), 
            "contraseña": random.choice(contraseñas),  
            "fecha_nacimiento": fechaInicio + timedelta(days=random.randint(0,10000)),  
            "fecha_registro": fechaInicio + timedelta(days=random.randint(0,2000))  
        }

        #Se genera una probabilidad entre 0 y 1
        probabilidadError = random.random()

        #Acá yo ya puedo ir poniendo errores con base a la probabilidad que yo quierao necesite 

        if probabilidadError < 0.1:
            simulacion["email"] = random.choice([
                simulacion["email"].replace("@",""),   # Esto elimina el @
                simulacion["email"] + " ",             #Esto pone un espacio al final
                simulacion["email"].replace(".com","") #Esto quita el dominio
            ])

        elif probabilidadError < 0.2:
            simulacion["telefono"] = random.choice([
                simulacion["telefono"][:-2],   #Esto hace que el número esté incompleto (tiene -2 digitos)
                " " + simulacion["telefono"], #Esto pone un espacio al inicio
                simulacion["telefono"] + "99" #Esto hace que el número sea más largo
            ])

        elif probabilidadError < 0.3:
            simulacion["id"]=random.choice([-1,-10,0]) #Valor no válido para ID

        elif probabilidadError < 0.5:
            simulacion["fecha_nacimiento"] = simulacion["fecha_nacimiento"].strftime("%d/%m") #Fecha con mal formato

        elif probabilidadError < 0.6:
            #Ubicación inconsistente (problema de estandarización)
            simulacion["ubicacion"] = random.choice([
                simulacion["ubicacion"].lower(),  # minúscula
                simulacion["ubicacion"].upper(),  # mayúscula
                simulacion["ubicacion"] + " ",    # espacio al final
                " " + simulacion["ubicacion"]     # espacio al inicio
            ])

        elif probabilidadError < 0.7:
            simulacion["nombre"] = random.choice([
                simulacion["nombre"].lower(),  # minúscula
                simulacion["nombre"].upper(),  # mayúscula
                " " + simulacion["nombre"],    # espacio al inicio
                simulacion["nombre"] + " "     # espacio al final
            ])

        elif probabilidadError < 0.8:
            
            simulacion["apellido"] = random.choice([
                simulacion["apellido"][:3],  #Apellido recortado
                simulacion["apellido"] + " ", #Apellido con espacio al final
                ""                           #Apellido vacío
            ])

        elif probabilidadError < 0.9:
            simulacion["fecha_registro"] = random.choice([
                datetime(2030,1,1),  # fecha futura
                datetime(1978,1,1)   # fecha muy antigua
            ])

    
        # Acá guardo la simulación (con o sin error)
        simulaciones.append(simulacion)

    #Agrega un duplicado 
    if len(simulaciones) >= 2:
        simulaciones.append(simulaciones[0].copy())

    return simulaciones
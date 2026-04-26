import pandas as pd 


def limpiar_simulacion_errores_usuaria(data_frame):
    data_frame_limpio=data_frame.copy()

    #1. Limpiar los espacios en blanco de las columnas de texto
    datos_texto=["nombre", "apellido", "email", "telefono", "ubicacion"]
    for columna in datos_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip()

    #2. Eliminar filas con valores faltantes
    ubicaciones_validas=["Bogotá","Medellín","Cali","Barranquilla","Cartagena"] #crea una lista de lo que sirve
    data_frame_limpio["ubicacion"]=data_frame_limpio["ubicacion"].where(
        data_frame_limpio["ubicacion"].isin(ubicaciones_validas), #esto dice que solo deje los que están en la lista
        pd.NA
    )

    
    
    

    #3.Convertir columnas numéricas
    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"]) #esto convierte a numérico y si no 
    #puede lo pone como NA   

    #4. Convertir la columna a fecha valida
    data_frame_limpio["fecha_nacimiento"]=pd.to_datetime(data_frame_limpio["fecha_nacimiento"], errors="coerce")
    data_frame_limpio["fecha_registro"]=pd.to_datetime(data_frame_limpio["fecha_registro"], errors="coerce")

    #5. Reemplazar un valor que venga nulo a uno por defefecto en este caso, fechas nulas se reemplazan por 
    # la fecha de inicio
    fecha_defecto=pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha_nacimiento"]=data_frame_limpio["fecha_nacimiento"].fillna(fecha_defecto)
    data_frame_limpio["fecha_registro"]=data_frame_limpio["fecha_registro"].fillna(fecha_defecto)

    #6. Eliminar filas que traen datos obligatorios vacíos 
    columnas_obligatorias=["id","nombre","email", "telefono","ubicacion"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    #7. Eliminar valores inválidos en la columna id (valores negativos o del valor menor que tenga en 
    # mis datos)    
    data_frame_limpio=data_frame_limpio[data_frame_limpio["id"] > 0]

    data_frame_limpio=data_frame_limpio[data_frame_limpio['telefono'].str.len() == 10]


    #8. Eliminar duplicados
    data_frame_limpio=data_frame_limpio.drop_duplicates()

    #9. Normalizar texto
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].str.title() #Esto pone la primera letra en mayúscula
    data_frame_limpio["apellido"] = data_frame_limpio["apellido"].str.title()
    data_frame_limpio["email"] = data_frame_limpio["email"].str.lower() #Esto pone todo en minúscula
    data_frame_limpio["ubicacion"] = data_frame_limpio["ubicacion"].str.title()
    
    return data_frame_limpio

    
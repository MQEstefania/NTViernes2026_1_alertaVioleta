import pandas as pd 

def limpiar_simulacion_errores_usuaria(data_frame):
    data_frame_limpio = data_frame.copy()

    #1. Limpiar espacios
    datos_texto = ["nombre", "apellido", "email", "telefono", "ubicacion"]
    for columna in datos_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()

    #2. Normalizar texto (ANTES de validar)
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].str.title()
    data_frame_limpio["apellido"] = data_frame_limpio["apellido"].str.title()
    data_frame_limpio["email"] = data_frame_limpio["email"].str.lower()
    data_frame_limpio["ubicacion"] = data_frame_limpio["ubicacion"].str.title()

    #3. Validar ubicaciones
    ubicaciones_validas = ["Bogotá","Medellín","Cali","Barranquilla","Cartagena"]
    data_frame_limpio["ubicacion"] = data_frame_limpio["ubicacion"].where(
        data_frame_limpio["ubicacion"].isin(ubicaciones_validas),
        pd.NA
    )

    #4. Convertir ID
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")

    #5. Convertir fechas
    data_frame_limpio["fecha_nacimiento"] = pd.to_datetime(data_frame_limpio["fecha_nacimiento"], format="mixed", errors="coerce")
    data_frame_limpio["fecha_registro"] = pd.to_datetime(data_frame_limpio["fecha_registro"], format="mixed", errors="coerce")

    #6. Reemplazar un valor que venga nulo a uno por defefecto en este caso, fechas nulas se reemplazan por 
    # la fecha de inicio
    fecha_defecto = pd.to_datetime("2026-01-01")

    #Eliminar fechas inválidas (NO rellenar), eso tendría mejor lógica que reemplazar, para no inventar datos.
    #data_frame_limpio = data_frame_limpio.dropna(subset=["fecha_nacimiento", "fecha_registro"])
    
    #7. Eliminar obligatorios vacíos
    columnas_obligatorias = ["id","nombre","apellido","email","telefono","ubicacion"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    #8. Validar ID
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]

    #9. Validar teléfono
    data_frame_limpio = data_frame_limpio[
        (data_frame_limpio["telefono"].str.len() == 10) &
        (data_frame_limpio["telefono"].str.isnumeric())
    ] #Esto es para que tenga una longitud de 10 dígitos y solo sean #s

    #10. Validar email
    data_frame_limpio = data_frame_limpio[data_frame_limpio["email"].str.contains("@", na=False)] #Esto es para que el email tenga un @, el na=False es para que no de error si hay valores nulos en email, 
    #los cuales ya se eliminaron en el paso 7 pero es una buena práctica ponerlo.

    #11. Filtrar fechas reales
    data_frame_limpio = data_frame_limpio[data_frame_limpio["fecha_nacimiento"] >= "1900-01-01"] #Esto es para eliminar fechas de nacimiento que sean muy antiguas, lo cual no sería realista.
    data_frame_limpio = data_frame_limpio[data_frame_limpio["fecha_registro"] <= pd.Timestamp.now()] #esto es para eliminar fechas de registro que sean futuras, lo cual no sería realista.

    #12. Eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio

    
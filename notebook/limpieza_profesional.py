import pandas as pd


def limpiar_simulacion_errores_profesional(data_frame):
    data_frame_limpio = data_frame.copy()

    # 1. Limpiar los espacios en blanco de las columnas de texto
    datos_texto = ["nombre", "apellido", "email", "telefono", "profesion"]
    for columna in datos_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip()

    # 2. Validar que la profesión sea una de las permitidas
    profesiones_validas = ["Abogado", "Medico", "Ingeniero", "Arquitecto", "Profesor"]
    data_frame_limpio["profesion"] = data_frame_limpio["profesion"].where(
        data_frame_limpio["profesion"].str.title().isin(profesiones_validas),  # solo deja los que están en la lista
        pd.NA
    )

    # 3. Convertir columnas de IDs a numérico (si no puede, lo pone como NA)
    data_frame_limpio["id_profesional"] = pd.to_numeric(data_frame_limpio["id_profesional"], errors="coerce")
    data_frame_limpio["id_usuaria"]     = pd.to_numeric(data_frame_limpio["id_usuaria"],     errors="coerce")
    data_frame_limpio["id_cliente"]     = pd.to_numeric(data_frame_limpio["id_cliente"],     errors="coerce")

    # 4. Convertir la columna fecha a fecha válida
    data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"], errors="coerce")

    # 5. Reemplazar fechas nulas por una fecha por defecto
    fecha_defecto = pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha"] = data_frame_limpio["fecha"].fillna(fecha_defecto)

    # 6. Eliminar filas que traen datos obligatorios vacíos
    columnas_obligatorias = ["id_profesional", "id_usuaria", "nombre", "email", "telefono", "profesion"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # 7. Eliminar valores inválidos en las columnas de ID (negativos o cero)
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_profesional"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_usuaria"]     > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_cliente"]     > 0]

    # 8. Eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    # 9. Normalizar texto
    data_frame_limpio["nombre"]    = data_frame_limpio["nombre"].str.title()     # Primera letra en mayúscula
    data_frame_limpio["apellido"]  = data_frame_limpio["apellido"].str.title()
    data_frame_limpio["email"]     = data_frame_limpio["email"].str.lower()      # Todo en minúscula
    data_frame_limpio["profesion"] = data_frame_limpio["profesion"].str.title()

    return data_frame_limpio
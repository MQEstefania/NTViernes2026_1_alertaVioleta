import pandas as pd


# Función para describir la estructura general del data frame
def describir_estructura(data_frame_limpio):
    print("***** Estructura general *****")
    print(f"Número de filas:    {data_frame_limpio.shape[0]}")
    print(f"Número de columnas: {data_frame_limpio.shape[1]}")
    print(f"Columnas disponibles: {list(data_frame_limpio.columns)}")


# Función para describir estadísticas generales del data frame
def describir_estadisticas(data_frame_limpio):
    print("\n***** Estadísticas *****")
    print(data_frame_limpio[["id_profesional", "id_usuaria", "id_cliente"]].describe())


# Función para medir columnas categóricas
def describir_categorias(data_frame_limpio):
    print("\n***** Frecuencias categóricas *****")

    print("Profesiones registradas:")
    print(data_frame_limpio["profesion"].value_counts())

    print("\nNombres más frecuentes:")
    print(data_frame_limpio["nombre"].value_counts())

    print("\nApellidos más frecuentes:")
    print(data_frame_limpio["apellido"].value_counts())


# Función para describir los rangos de fechas
def describir_fechas(data_frame_limpio):
    print("\n***** Fechas *****")
    print(f"Fecha más antigua: {data_frame_limpio['fecha'].min()}")
    print(f"Fecha más reciente: {data_frame_limpio['fecha'].max()}")


# Función principal que llama a todas las anteriores
def describir_todo(data_frame_limpio):
    describir_estructura(data_frame_limpio)
    describir_estadisticas(data_frame_limpio)
    describir_categorias(data_frame_limpio)
    describir_fechas(data_frame_limpio)
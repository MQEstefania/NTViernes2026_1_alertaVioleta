import pandas as pd

#Función para describir la estructura general del data set
def describir_estructura(data_frame_limpio):
    print("**** Estructura general ****")
    print(f"Numero de filas: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas: {data_frame_limpio.shape[1]}")
    print(f"Columnas disponibles: {list(data_frame_limpio.columns)}")

#Función para describir estadísticas del data frame 
def describir_estadisticas(data_frame_limpio):
    print("\n**** Estadísticas *****")
    print(f"{data_frame_limpio[["id"]].describe()}")

#Función para medir las columnas categóricas (la frecuencia en la que aparecen las categorías ej: la ciudad más peligrosa)
def describir_categoricas(data_frame_limpio):
    print("\n**** Frecuencias categóricas ****")
    print("Nombres")
    print(f"{data_frame_limpio["nombre"].value_counts()}")
    
    print("\nUbicaciones:")
    print(data_frame_limpio["ubicacion"].value_counts())

    print("\nCorreos:")
    print(data_frame_limpio["email"].value_counts())

#Función para describir los rangos de fechas
def describir_fechas(data_frame_limpio):
    print("\n**** Rango de fechas ****")
    print(f"Fecha de nacimiento mínima: {data_frame_limpio["fecha_nacimiento"].min()}")
    print(f"Fecha de nacimiento máxima: {data_frame_limpio["fecha_nacimiento"].max()}")

    print(f"\nFecha de registro mínima: {data_frame_limpio["fecha_registro"].min()}")
    print(f"Fecha de registro máxima: {data_frame_limpio["fecha_registro"].max()}")


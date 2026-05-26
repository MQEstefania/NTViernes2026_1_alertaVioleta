import pandas as pd

def limpiar_contactos(contactos):

    df = pd.DataFrame(contactos)

    # Eliminar nombres vacíos
    df = df[df["nombre"] != ""]

    # Eliminar relaciones nulas
    df = df[df["relacion"].notnull()]

    # Eliminar teléfonos inválidos
    df = df[df["telefono"] != "ERROR"]

    return df
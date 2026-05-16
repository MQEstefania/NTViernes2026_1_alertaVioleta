import pandas as pd

def describir_contactos(df):

    print("\n--- DESCRIPCION CONTACTOS EMERGENCIA ---\n")

    print(df.info())

    print("\nESTADISTICAS:\n")
    print(df.describe(include="all"))

    print("\nVALORES NULOS:\n")
    print(df.isnull().sum())
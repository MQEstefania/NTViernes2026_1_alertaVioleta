
import pandas as pd

#Acá estoy importando las funciones
from simulacion_errores_usuaria import generar_simulacion_errores_usuaria
from notebook.limpieza_usuaria import limpiar_simulacion_errores_usuaria

datos_simulacion = generar_simulacion_errores_usuaria(10) #Generar datos ( esto son los que ya vienen con errores)

df = pd.DataFrame(datos_simulacion) #Acá se va a convertir a DataFrame

df_limpio = limpiar_simulacion_errores_usuaria(df) #Acá se va a limpiar los datos

#simulaciones_limpias=limpiar_simulacion(simulaciones_ordenadas)
#print(simulaciones_ordenadas_limpias) #Imprimimos el DataFrame limpio para verificar los resultados de 
#la limpieza y asegurarnos de que los datos estén en el formato correcto y sin errores. Esto me arrojó error
#la ia me explicó que esas funciones no existen, por lo que me mandó a imprimir así: 

# Mostrar resultados
print("DATOS SUCIOS")
print(df)

print("\nDATOS LIMPIOS")
print(df_limpio)
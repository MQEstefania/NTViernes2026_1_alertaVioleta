
import pandas as pd

# ===== USUARIAS =====
from util.simulacion_errores_usuaria import generar_simulacion_errores_usuaria
from notebook.limpieza_usuaria import limpiar_simulacion_errores_usuaria
from notebook.descripcion_usuaria import (
    describir_estructura,
    describir_estadisticas,
    describir_categoricas,
    describir_fechas
)

print("\n===== USUARIAS =====")

# 🔹 Simulación (con errores)
simulaciones_usuaria = generar_simulacion_errores_usuaria(10)

# 🔹 Convertir a DataFrame
df_usuaria = pd.DataFrame(simulaciones_usuaria)

# 🔹 Mostrar datos sucios
print("\nDATOS SUCIOS (con errores)")
print(df_usuaria)

# 🔹 Limpieza
df_usuaria_limpio = limpiar_simulacion_errores_usuaria(df_usuaria)

# 🔹 Mostrar datos limpios
print("\nDATOS LIMPIOS")
print(df_usuaria_limpio)

# 🔹 Análisis
print("\n--- ANÁLISIS USUARIAS ---")
describir_estructura(df_usuaria_limpio)
describir_estadisticas(df_usuaria_limpio)
describir_categoricas(df_usuaria_limpio)
describir_fechas(df_usuaria_limpio)


# ===== PROFESIONALES =====
from util.simulacion_errores_profesionales import generar_simulacion_errores_profesional
from notebook.limpieza_profesional import limpiar_simulacion_errores_profesional
from notebook.descripcion_profesional import (
    describir_estructura,
    describir_estadisticas,
    describir_categoricas,
    describir_fechas
)

print("\n===== PROFESIONALES =====")

# 🔹 Simulación (con errores)
simulaciones_prof = generar_simulacion_errores_profesional(10)

# 🔹 Convertir a DataFrame
df_prof = pd.DataFrame(simulaciones_prof)

# 🔹 Mostrar datos sucios
print("\nDATOS SUCIOS (con errores)")
print(df_prof)

# 🔹 Limpieza
df_prof_limpio = limpiar_simulacion_errores_profesional(df_prof)

# 🔹 Mostrar datos limpios
print("\nDATOS LIMPIOS")
print(df_prof_limpio)

# 🔹 Análisis
print("\n--- ANÁLISIS PROFESIONALES ---")
describir_estructura(df_prof_limpio)
describir_estadisticas(df_prof_limpio)
describir_categoricas(df_prof_limpio)
describir_fechas(df_prof_limpio)
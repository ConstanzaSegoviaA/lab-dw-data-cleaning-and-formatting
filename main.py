import pandas as pd
from limpieza_utils import (
    limpiar_nombres_columnas, 
    limpiar_texto, 
    gestionar_nulos_y_duplicados, 
    informe_detallado
)

def ejecutar_limpieza_total(ruta_archivo):
    # 1. Cargar datos
    df = pd.read_csv(ruta_archivo)
    
    # 2. Pipeline de limpieza
    df = limpiar_nombres_columnas(df)
    df = gestionar_nulos_y_duplicados(df)
    df = limpiar_texto(df)
    
    # 3. Informe final
    informe_detallado(df)
    
    # 4. Guardar resultado
    df.to_csv('datos_finales_2026.csv', index=False)
    print("\nProceso finalizado. Archivo 'datos_finales_2026.csv' creado.")
    return df

if __name__ == "__main__":
    # Cambia 'tu_archivo.csv' por el nombre real de tu archivo
    ejecutar_limpieza_total('tu_archivo.csv')

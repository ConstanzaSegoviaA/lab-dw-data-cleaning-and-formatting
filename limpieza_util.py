import pandas as pd

def limpiar_nombres_columnas(df):
    """Normaliza los nombres de las columnas: minúsculas y guiones bajos."""
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

def limpiar_clv(df[x]):
    
    # Limpia la columna 'customer_lifetime_value' eliminando el símbolo '%' 
    # y convirtiéndola a tipo numérico (float).
    col = x
    if col in df.columns:
        # Convertimos a string, quitamos '%' y convertimos a float
        df[col] = df[col].astype(str).str.replace('%', '', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Opcional: si el dato original era "1288743.17%", 
        # al quitar el % queda un número muy grande.      
    return df


def limpiar_texto(df):
    """Limpia espacios y normaliza texto en columnas de tipo objeto."""
    df_limpio = df.copy()
    for col in df_limpio.select_dtypes(include=['object']):
        df_limpio[col] = df_limpio[col].astype(str).str.strip().str.upper()
    return df_limpio

def gestionar_nulos_y_duplicados(df):
    """Elimina duplicados y filas con valores nulos."""
    df = df.drop_duplicates().reset_index(drop=True)
    df = df.dropna().reset_index(drop=True)
    return df

def informe_detallado(df):
    """Imprime un resumen completo del estado del DataFrame."""
    print("--- INFORME DE DATOS ---")
    print(f"Forma: {df.shape}")
    print("\nValores Nulos por Columna:")
    print(df.isnull().sum())
    print("\nTipos de Datos:")
    print(df.dtypes)
    return df
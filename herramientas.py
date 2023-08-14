import pandas as pd
# muestra los valores unicos por columna
def obtener_resumen_valores_unicos(df):
    # Obtener el número de valores únicos en cada columna
    valores_unicos = df.nunique()

    # Obtener el número total de valores en cada columna (no nulos)
    total_valores = df.count()

    # Obtener el número de valores nulos en cada columna
    valores_nulos = df.isnull().sum()

    # Obtener los tipos de datos de cada columna
    tipos_datos = df.dtypes

    # Combinar los resultados en un nuevo DataFrame
    resumen_valores_unicos = pd.DataFrame({
        'Columna': valores_unicos.index,
        'Tipo de Dato': tipos_datos.values,
        'Valores Únicos': valores_unicos.values,
        'Total Valores': total_valores.values,
        'Valores Nulos': valores_nulos.values
    })
    
    return resumen_valores_unicos
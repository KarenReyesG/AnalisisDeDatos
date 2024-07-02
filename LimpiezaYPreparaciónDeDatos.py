#Parte 5: Limpieza y preparación de datos
#Una vez cargado el csv mediante el request anterior, realiza lo siguiente:

#Verificar que no existan valores faltantes
#Verificar que no existan filas repetidas
#Verificar si existen valores atípicos y eliminarlos
#Crear una columna que categorice por edades
#0-12: Niño
#13-19: Adolescente
#20-39: Jóvenes adulto
#40-59: Adulto
#60-...: Adulto mayor
#Guardar el resultado como csv
#Encapsula toda la lógica anterior en una función que reciba un dataframe como entrada.


import pandas as pd

def clean_and_prepare_data(df):
    # Verificar que no existan valores faltantes
    if df.isnull().values.any():
        print("Existen valores faltantes. Se reemplazan por la media.")
        df.fillna(df.mean(), inplace=True)

    # Verificar que no existan filas repetidas
    if df.duplicated().sum() > 0:
        print("Existen filas repetidas. Se eliminan.")
        df.drop_duplicates(inplace=True)

    # Verificar si existen valores atípicos y eliminarlos
    for col in df.select_dtypes(include=['int64', 'float64']):
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]

    # Crear una columna que categorice por edades
    df['Edad_Categoria'] = pd.cut(df['age'], bins=[0, 12, 19, 39, 59, 150], 
                                 labels=['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor'])

    return df

# Cargar el csv
df = pd.read_csv('C:/Users/HP USER/Desktop/ADA SCHOOL/ANALISIS DE DATOS/heart_failure_data.csv')

# Llamar a la función
df = clean_and_prepare_data(df)

# Guardar el resultado como csv
df.to_csv('C:/Users/HP USER/Desktop/ADA SCHOOL/ANALISIS DE DATOS/heart_failure_data_ETL.csv', index=False)
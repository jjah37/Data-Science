import pandas as pd

# Diccionario de ejemplo
data = {
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [23, 30, 27],
    "Ciudad": ["Quito", "Guayaquil", "Cuenca"]
}

# Convertir el diccionario en un DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
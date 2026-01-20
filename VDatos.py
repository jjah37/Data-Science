import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Diccionario de datos
data = {
    "Nombre": ["Ana", "Luis", "Carlos", "María", "José"],
    "Edad": [23, 30, 27, 22, 35],
    "Ciudad": ["Quito", "Guayaquil", "Cuenca", "Quito", "Guayaquil"],
    "Salario": [1200, 1500, 1100, 1000, 2000]
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame
print("DataFrame generado:\n")
print(df)

# --- Visualización con matplotlib ---
plt.figure(figsize=(6,4))
plt.bar(df["Nombre"], df["Salario"], color="skyblue")
plt.title("Salario por persona")
plt.xlabel("Nombre")
plt.ylabel("Salario")
plt.show()

# --- Visualización con seaborn (scatterplot) ---
plt.figure(figsize=(6,4))
sns.scatterplot(x="Edad", y="Salario", hue="Ciudad", data=df, s=100)
plt.title("Relación Edad vs Salario")
plt.show()

# --- Visualización con seaborn (boxplot) ---
plt.figure(figsize=(6,4))
sns.boxplot(x="Ciudad", y="Salario", data=df)
plt.title("Distribución de salarios por ciudad")
plt.show()




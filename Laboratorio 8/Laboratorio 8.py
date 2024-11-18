#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos
data = {
    "Producto": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Bogotá": [500, 400, 300, 200, 100, 450, 350, 250],
    "Cali": [450, 350, 300, 200, 150, 400, 300, 200],
    "Bucaramanga": [300, 250, 200, 150, 100, 350, 300, 250],
}

df = pd.DataFrame(data)

# Gráfico
plt.style.use("seaborn-darkgrid")
df.set_index("Producto").plot(kind="bar", figsize=(10, 6), colormap="viridis")
plt.title("Ventas de productos en tres ciudades", fontsize=16)
plt.ylabel("Ventas")
plt.xlabel("Productos")
plt.legend(title="Ciudad")
plt.tight_layout()
plt.show()


# In[2]:


# Datos
data = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto"],
    "Papa (Cali)": [100, 150, 200, 250, 300, 400, 300, 150],
    "Cebolla (Bogotá)": [90, 120, 160, 200, 240, 100, 200, 150],
    "Tomate (Cartagena)": [80, 110, 150, 190, 230, 330, 350, 240],
}

df = pd.DataFrame(data)

# Gráfico
plt.figure(figsize=(10, 6))
for producto in df.columns[1:]:
    plt.plot(df["Mes"], df[producto], marker="o", label=producto)

plt.title("Evolución de ventas de productos", fontsize=16)
plt.ylabel("Ventas")
plt.xlabel("Mes")
plt.xticks(rotation=45)
plt.legend(title="Producto (Ciudad)")
plt.grid(alpha=0.3)
plt.show()


# In[3]:


# Datos
data = {
    "Horas Estudiadas": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "Puntuación": [50, 60, 65, 70, 75, 78, 80, 82, 85, 87, 90, 92, 94, 96, 98],
    "Motivación": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],
}

df = pd.DataFrame(data)

# Gráfico
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="Horas Estudiadas",
    y="Puntuación",
    size="Motivación",
    sizes=(20, 200),
    hue="Motivación",
    palette="coolwarm",
)
plt.title("Relación entre horas estudiadas y puntuación", fontsize=16)
plt.xlabel("Horas Estudiadas")
plt.ylabel("Puntuación")
plt.legend(title="Nivel de Motivación")
plt.grid(alpha=0.3)
plt.show()


# In[4]:


# Datos
data = {
    "Puntuación": [50, 60, 65, 70, 75, 78, 80, 82, 85, 87, 90, 92, 94, 96, 98],
    "Motivación": [
        "Baja", "Media", "Media", "Alta", "Alta", "Media", "Media", "Alta",
        "Alta", "Baja", "Alta", "Alta", "Media", "Alta", "Alta",
    ],
}

df = pd.DataFrame(data)

# Gráfico
plt.figure(figsize=(10, 6))
sns.histplot(
    data=df,
    x="Puntuación",
    hue="Motivación",
    multiple="stack",
    palette="viridis",
    kde=True,
    bins=10,
)
plt.title("Distribución de puntuaciones según motivación", fontsize=16)
plt.xlabel("Puntuación")
plt.ylabel("Frecuencia")
plt.show()


# In[5]:


# Datos
data = {
    "Mes": [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
        "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
    ],
    "SUV": [120, 130, 135, 140, 150, 160, 170, 180, 175, 185, 190, 200],
    "Sedan": [100, 90, 95, 110, 120, 130, 140, 145, 150, 160, 170, 180],
    "Hatchback": [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135],
}

df = pd.DataFrame(data)

# Gráfico
plt.figure(figsize=(10, 6))
df.plot(x="Mes", kind="line", marker="o", figsize=(10, 6), colormap="plasma")
plt.title("Ventas mensuales de vehículos", fontsize=16)
plt.ylabel("Ventas")
plt.xlabel("Mes")
plt.legend(title="Tipo de Vehículo")
plt.grid(alpha=0.3)
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importación de bibliotecas necesarias
import pandas as pd
import numpy as np


# In[2]:


# Parte 1: Uso de Pandas
print("Parte 1: Uso de Pandas\n")

# Ejercicio 1.1: Crear un DataFrame con nombres, profesión y países
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Sofía', 'Carlos', 'Lucía', 'Pedro', 'Marta'],
    'Profesión': ['Ingeniero', 'Doctor', 'Arquitecto', 'Maestra', 'Abogado', 'Diseñadora', 'Programador', 'Contadora'],
    'País': ['Colombia', 'España', 'México', 'Argentina', 'Chile', 'Perú', 'Brasil', 'Uruguay']
}
df_personas = pd.DataFrame(data)
print("DataFrame con Nombres, Profesión y País:")
print(df_personas, "\n")


# In[3]:


# Ejercicio 1.2: Cargar un archivo CSV y mostrar las primeras 5 filas
# Asegúrate de tener un archivo llamado 'data.csv' en el mismo directorio.
try:
    df_csv = pd.read_csv("data.csv")
    print("Archivo CSV cargado - Primeras 5 filas:")
    print(df_csv.head(), "\n")
except FileNotFoundError:
    print("El archivo 'data.csv' no se encontró. Por favor verifica su ubicación.\n")


# In[4]:


# Ejercicio 1.3: Crear un DataFrame aleatorio con 100 filas y 8 columnas
df_random = pd.DataFrame(np.random.rand(100, 8), columns=[f"Col_{i}" for i in range(1, 9)])
print("Resumen estadístico del DataFrame aleatorio:")
print(df_random.describe(), "\n")


# In[5]:


# Parte 2: Uso de NumPy
print("Parte 2: Uso de NumPy\n")

# Ejercicio 2.1: Operaciones con un array de números del 1 al 10
array = np.arange(1, 11)
print("Array de números del 1 al 10:", array)
print("Suma total:", np.sum(array))
print("Media:", np.mean(array))
print("Valor máximo:", np.max(array), "\n")


# In[6]:


# Ejercicio 2.2: Crear un array de 3x4 lleno de ceros y cambiar su forma a 2x6
array_zeros = np.zeros((3, 4))
print("Array 3x4 lleno de ceros:")
print(array_zeros)
array_zeros_reshaped = array_zeros.reshape(2, 6)
print("Array 2x6 después de cambiar la forma:")
print(array_zeros_reshaped, "\n")


# In[7]:


# Ejercicio 2.3: Generar una matriz aleatoria 3x3 y calcular su transpuesta
matrix = np.random.rand(3, 3)
print("Matriz aleatoria 3x3:")
print(matrix)
print("Matriz transpuesta:")
print(matrix.T, "\n")


# In[8]:


# Ejercicio 2.4: Concatenar dos arrays y mostrar el resultado
array1 = np.random.randint(1, 50, 5)
array2 = np.random.randint(50, 100, 5)
concatenated_array = np.concatenate((array1, array2))
print("Array concatenado:")
print(concatenated_array)


# In[ ]:





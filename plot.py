from matplotlib import pyplot as plt
import numpy as np
def graficar_pesos_capa(pesos, nombre_capa):
  """
  Grafica la distribución de pesos para una capa específica.

  Parámetros:
    pesos (list): Lista que contiene los valores de los pesos de la capa.
    nombre_capa (str): Nombre de la capa a graficar.

  Retorno:
    None: Muestra los gráficos de la distribución de pesos para la capa indicada.
  """
  # Eliminar valores no numéricos
  # pesos = list(filter(lambda x: x.isdigit(), pesos))
  # pesos = np.array(pesos, dtype=float)

  # Calcular la media
  # media = np.mean(pesos)

  # Calcular la mediana
  pesos = pesos.split(" ")


  #Arreglar el float formatting


  # Convertir la lista a un tipo de dato numérico
  pesos = np.array(pesos, dtype=float)

 
 
  for peso in pesos:
    print(type(peso))
  mediana = np.median(pesos)

  # Generar histograma
  plt.hist(pesos, bins=pesos.shape, color="skyblue", alpha=0.7)
  plt.xlabel("Pesos Capa " + nombre_capa)
  plt.ylabel("Frecuencia")
  plt.title("Distribución de pesos - Capa 1 (Mediana: {})".format(mediana))
  plt.show()

# Ejemplo de uso
"""
input1 = "5.49 4.05 5.36 5.65 5.67 4.88 4.05 5.33 3.71 5.4 5.42 4.67 4.32 5.47 5.17 4.08 4.83 4.5 5.19 4.99 5.32 5 5.36 5.08 4.5 4.73 5.2 3.9 4.32 3.69 3.45 3.86 3.82 4.9 3.63 3.63 3.95 3.87 3.17 3.89 3.52 4.87 4.87 4.17 4.7 4.41 4.65 3.94 3.43 4.56 3.72 3.63 4.5 4.1 3.7 3.92 3.85 4.05 4.99 5.3 4.79 5.64 6.42 5.98 5.87 5.36 6.96 7.21 6.64 5.55 6.42 7.53 5.79 6.83 7.21 8 6.71 7.36 7.43 7.58 7.2 8.54 8.54 8.79 7.61 8.98 7.42 7.97 7.51 8.83 9.55 8.48 8.48 9.87 8.2 9.89 8.71 10.46 10.17 10.34 8.87 9.42 10.51 9.16 10.56 9.95 11.4 11.34 11.42 10.94 10.94 10.56 11.23 11.02 10.75 12.05 11.19 11.27 13.07 11.58 12.94 13.36 12.67 13.74 13.46 12.99 13.54 14.03 13.17 13.21 13.57 13.1 13.57 12.94 13.07 12.81 13.51 12.95 12.52 13.12 13.89 13.3 13.35 12.61 13.68 13.37 11.81 11.89 13.56 13.64 12.11 12.92 13.32 12.99 12.74 12.78 11.88 12.1 12.48 12.68 12.97 11.74 11.49 12.28 12.46 12.37 12.92 11.83 11.2 11.35 12.89 11.06 12.64 12.26 11.72 12.4 11.75 11.67 12.46 11.5 11.53 10.82 12.7 11.16 12.14 11.81 12.34 12.44 12.35 11.3 11.63 11.86 11.61 11.72 10.77 10.72 10.77 10.4 11.29 10.75 10.55 11.01 10.67 10.09 10.2 11.34 11.48 10.96 10.05 11.02 11.56 10.71 11 11.46 11.1 10.4 10.55 10.76 10.19 10.28 11.46 11.27 9.62 10.58 10.53 9.96 10.9 10.93 10.03 9.88 9.41 10.34 10.68 9.9 10.29 10.77 9.15 9.72 9.71 9.21 10.78 9.36 10.04 9.93 8.99 9.35 10.58 9.82 10.41 9.12 8.48 10.29 8.83 8.58 9.37 9.9"
input2 = "3.12 2.13 3.64 4.29 4.08 3.83 2.71 3.72 2.08 3.16 3.84 3.2 3.39 4.97 4.2 3.39 3.29 3.19 3.77 3.99 4.85 3.83 5.83 4.77 4.23 5.51 5.01 4.3 3.56 4.77 3.64 4.16 3.77 4.72 3.8 3.14 5.44 5.19 3.78 3.99 5.19 6.8 6.03 5.21 6.46 4.71 5.06 5.95 3.56 5.44 4.16 5.09 4.89 4.94 4.38 5.88 4.31 5.61 7.25 6.97 7 9.26 10.12 8.17 8.15 7.54 9.92 10.54 10.97 9.15 10.03 13.34 9.17 12.09 11.77 12.91 12.1 12.67 12.34 12.4 12.73 14.76 16.21 16.58 13.9 15.69 14.38 14.88 14.38 15.82 17.94 16.16 15.65 18.98 16.16 19.16 17.44 21 19.79 21.24 17.02 20.11 21.54 18.68 22.1 21.47 25.11 24.01 23.76 22.54 23.95 22 24.36 24.64 23.07 25.89 25.33 26.24 30.13 26.46 28.76 30.99 28.71 31.74 32.55 30.89 32.26 33.53 31.19 31.56 32.38 31.77 32.58 32.32 33.48 32.51 34.13 33.49 31.36 34.51 36.6 35.18 33.78 32.77 35.73 34.51 31.19 30.84 35.18 35.8 32.91 34.11 36.3 35.83 34.69 35.16 32.37 32.71 33.83 35.31 35.96 32.34 32.94 34.48 35.94 35.65 36.09 33.6 32.37 32.45 37.03 32.23 36.45 35.75 35.45 37.06 34.94 34.65 37.91 34.6 34.9 32.69 38.83 33.3 36.54 35.32 38.33 38.45 37.59 35.6 37.21 37.03 37.21 37.3 34.58 34.22 33.93 33.75 36.89 35.15 33.05 34.8 34.09 32.2 33.1 36.39 38.28 36.84 33.27 36.62 38.15 34.84 35.79 37.35 36.69 34.46 34.7 37.17 35.04 34.37 39.32 38.88 33.29 36.36 36.02 34.26 36.99 38.37 34.33 33.54 33.03 35.77 36.86 35.56 36.3 38.34 31.6 34.27 34.75 33.26 37.56 32.62 36.73 34.98 31.7 33.09 38.14 35.14 37.09 32.72 31.08 36.29 31.43 31.11 34.4 36.48"
graficar_pesos_capa(input1, "Capa 1")
graficar_pesos_capa(input2, "Capa 2")

input1 = "5.32 4.54 5.95 6.44 5.04 6.45 5 6.07 5.37 6.2 4.55 6.37 5.71 6.19 5.37 4.77 4.99 5.43 5.85 5.91 5.14 6.39 6.31 5.44 5.04 5.95 5.57 5.83 6.41 4.49 6.35 5.22 4.58 5.89 5.23 5.19 5.83 5.74 4.74 4.71 5.46 4.84 4.65 4.66 4.55 5.51 5 5.05 6.47 6.36 6.46 5.16 6.22 6.27 6.1 4.79 5.72 5.17 6.13 5.69 5.3 6.12 4.55 5.52 5.6 5.37 6.29 5.13 4.77 6.69 5.48 5.83 5.06 5.6 5.99 5.12 6.71 6.54 5.73 6.7 6.4 5.69 5.41 6.22 5.55 5.04 6.54 4.86 5.79 6.2 6.05 6.57 5.84 6.07 5.52 4.91 4.89 5.21 5.39 5.08 5.31 6.19 6.25 5.71 5.11 5.52 6.1 5.07 5.32 5.08 5.06 7 6.04 5.67 6.39 6.76 5.92 6.1 6.71 6.84 5.46 5.92 6.63 6.52 5.22 5.32 6.58 5.25 5.65 6.98 5.34 5.88 6.12 6.53 6.54 6.19 4.98 5.53 6.19 5.34 5.62 6.2 5.23 6.56 6.83 6.59 6.28 5.67 5.67 5.99 5.49 6.12 4.91 5.1 5.6 5.07 5.31 5.1 5.3 5.92 5.05 5.62 6.76 6.15 5.1 6.28 5.33 5.12 4.87 6.59 5.44 5.57 5.89 5.82 5.24 5.84 5.52 6.67 6.63 6.31 5.76 5.29 5.58 5.82 5.54 6.35 6.09 6.05 6.66 6.62 5.15 4.91 5.38 5.13 6.25 5.67 6.56 4.81 5.99 4.65 4.63 4.71 5.52 5.83 5.83 6.05 4.95 6.65 5.98 4.82 6.21 4.98 5.35 5.01 6.01 6.05 6.59 5.39 5.39 6.53 5.24 5.82 6.74 5.9 6.22 6.25 4.85 6.04 6.36 6.2 6.09 6.34 6.26 4.95 5.52 5.38 6.27 5.73 5.3 5.58 5.91 4.83 5.8 6.49 5.13 5.12 5.85 4.98 5.75 6.46 4.78 6.27 5.52 4.74 5.35 4.94"
input2 = "49.35 38.5 49.75 51.78 37.78 48.68 36.86 44.72 38.55 44.32 31.17 43.5 37.83 41.5 36.13 31.41 32.25 34.23 37.66 37.41 32.21 39.23 39.65 32.27 29.11 34.58 33.86 34.81 36.24 24.93 36.56 30.6 26.27 33.7 29 29.48 31.77 32.18 26.43 25.76 29.62 27.04 24.11 25.57 24.13 27.8 26.94 25.58 33.26 32.77 33.95 27.32 30.74 32.57 29.95 23.65 29.39 25.48 29.43 28.75 25.53 30.72 22.73 27.34 26.6 25.29 30.7 25.1 21.73 31.57 25.92 27.8 23.63 26.86 28.19 24.52 31.87 30.14 25.57 30.23 28.44 26.44 24.04 27.29 25.97 22.32 29.51 22.51 25.39 27.69 27.68 29.3 25.77 26.48 24.33 22.31 21.98 22.28 23.74 22.93 23.49 26.74 26.63 25.92 21.56 24.71 27.33 22.87 22.79 22.88 21.31 29.64 26.52 24.29 27.61 29.18 25.85 25.34 28.62 30 23.73 23.38 27.99 28.41 21.91 23.19 28.98 21.73 24.87 29.61 22.39 24.26 26.42 28 27.19 27.31 21.45 24.12 27.13 23 25 27.24 22.51 28.64 28.93 27.83 26.92 24.92 23.75 26.63 23.96 27.29 22.33 23.01 24.64 22.54 23.39 22.35 24.09 25.6 23.18 24.44 30.16 27.46 23.25 28.48 23.59 21.91 21.23 30.91 25.68 24.53 27.51 26.21 25.05 27.26 25.17 30.44 30.83 29.6 27.37 25.86 25.77 28.09 26.52 30.78 28.77 28.34 30.97 31.57 24.44 24.19 25.22 25.48 29.98 29 31.85 24.2 28.89 23.73 23.15 24.15 28.32 29.25 29.6 31.84 24.28 35.08 30.57 25.44 32.2 27.17 28.57 26.75 32.89 31.91 35.04 30.16 29.47 35.82 28.92 32.89 37.38 34 35.12 35.97 28.54 35.24 38.31 36.96 35.62 38.32 38.51 29.58 34.62 34.43 40.44 36.93 34.37 34.95 38.18 32.71 37.93 44.1 34.51 35.88 41.7 34.7 41.68 45.7 35.25 47.88 42.37 36.91 43.38 42.5"
graficar_pesos_capa(input1, "Capa 1")
graficar_pesos_capa(input2, "Capa 2")
"""
input1 = "1.11 0.9 1.48 1.83 0.43 0.42 1.09 0.52 1.3 0.85 0.25 2.02 0.1 0.1 1.16 1.38 1.81 1.51 0.38 0.18 1.52 1.25 1.28 1.42 1.27 1.02 0.27 0.21 1.5 0.24 1.86 0.41 0.94 1.15 0.05 1.2 1.41 0.98 1.58 0.58 1.71 1.71 0.49 1.72 1.72 1.57 1.03 1.47 1.03 1.37 1.61 0.52 0.61 0.88 -0.05 -0.11 -0.07 0.25 0.15 1.48 0.55 0.08 -0.03 -0.41 3.69 2.49 3.26 3.23 3.61 2.98 1.96 3.48 2.87 2.64 3.4 2.79 2.42 2.65 2.49 3.69 2.27 2.36 2.49 3.16 3.54 2.74 3.37 1.8 3.32 1.86 1.63 2.24 2.32 1.99 2.22 2.05 2.53 3.55 3.35 2.22 2.63 3.42 1.82 1.63 2.2 3.37 2.57 2.79 2.2 3.26 2.69 2.68 1.85 1.41 2.09 1.65 2.42 1.74 1.74 2.05 1.91 1.7 2.63 2.58 2.05 1.22 3.01 2.97 "
input2 = "38.33 31.86 52.98 66.93 14.14 13.38 39.32 16.75 47.48 29.94 7.62 76.65 0.74 1.38 42.73 51.73 68.92 57.9 12.66 3.81 59.44 48.32 48.78 54.57 50.05 38.41 9.45 6.19 58.14 8.49 73.55 13.73"
graficar_pesos_capa(input1, "Capa 1")
graficar_pesos_capa(input2, "Capa 2")

# -*- coding: utf-8 -*-
"""reto_10_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VdG0vJ3fudNihIQBU9gLOkZtVdnxT69I
"""

elementos = int(input("Cuantos elementos quieres mi bro? "))
numeros_reales= []
for total in range(elementos):
  total = float(input("Ingresa el número, que sea real por favor: "))
  numeros_reales.append(total)

suma_nums: int = 0
for i in numeros_reales:
  suma_nums += i
promedio = (suma_nums/len(numeros_reales))
print("El promedio de " +str(numeros_reales)+ " es " +str(promedio))
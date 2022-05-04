# ----------------------------------------------------------------
# Práctica 9: Cifrado RSA
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 05/05/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo de las funciones
# implementadas en la práctica.
# ----------------------------------------------------------------

import os
import random

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

# Algoritmo de exponenciación rápida
def quickExp(base, exp, module):
  x = 1
  y = base % module
  expCopy = exp
  while (expCopy > 0 and y > 1):
    if (expCopy % 2 != 0):
      x = (x * y) % module
      expCopy = expCopy - 1
    else:
      y = (y * y) % module
      expCopy = expCopy / 2
  return x

# Comprobar que un número es primo mediante el algoritmo de Lehman-Peralta
# p = número primo a comprobar si es primo o no
# aleatoryGeneration = cantidad de números aleatorios a utilizar
def lehmanPeralta(p, aleatoryGeneration):
  if (p != 2 and p != 3 and p != 5 and p != 7 and p != 11):
    if (p % 2 != 0 and p % 3 != 0 and p % 5 != 0 and p % 7 != 0 and p % 11 != 0):
      aleatoryNumbers = []
      if (aleatoryGeneration < p - 1): 
        aleatoryNumbers = random.sample(range(2, p), aleatoryGeneration)
      else:
        aleatoryNumbers = random.sample(range(2, p), p - 2)
      it = 0
      a = []
      while (it < len(aleatoryNumbers)):
        a.append(quickExp(aleatoryNumbers[it], (p - 1) / 2, p)) 
        it += 1
      it = 0
      while (it < len(a)):
        if (a[it] != 1):
          if (p - 1 in a):
            return True
          else:
            return False
        it += 1
    else:
      return False
  else:
    return True

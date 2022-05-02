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

# Limpia la pantalla de la terminal
def cleanTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')
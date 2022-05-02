# ----------------------------------------------------------------
# Práctica 9: Cifrado RSA
# Asignatura: Seguridad en Sistemas Informáticos
# Fecha de entrega: 05/05/2022
# Autor:
# - Adrián González Galván
# - alu0101321219@ull.edu.es
# ----------------------------------------------------------------
# En este fichero se incluye el desarrollo del menú de la práctica.
# ----------------------------------------------------------------

from functions import *
import sys

# Main
cleanTerminal()
print("\n PRÁCTICA 9: RSA\n")

# Lectura de opciones
key = input("  Clave: ")
if (len(key.replace(' ', '')) != 32):
  sys.exit('La clave introducida no es correcta...')
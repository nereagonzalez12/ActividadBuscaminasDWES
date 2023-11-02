from random import random

from .forms import CreaTableroForm

from .views import generar_minas

class Casilla:
    def __int__(self, fila, columna):
        self.fila=fila
        self.columna=columna
        self.isMina=False
        self.adyacentes=0


#clase tablero
class Tablero:
    def __init__(self, filas, columnas, nMinas):
        self.filas=CreaTableroForm.filas
        self.columnas=CreaTableroForm.columnas
        self.nMinas=CreaTableroForm.minas
        #genero la lista de coordenadas de las minas
        self.minas=generar_minas(filas, columnas, nMinas)
        #inicializo las casillas
        self.casillas = [[Casilla(fila, columna) for columna in range(columnas)] for fila in range(filas)]


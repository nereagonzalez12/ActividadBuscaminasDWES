from random import random

from .forms import CreaTableroForm

#from .views import generar_minas

class Casilla:
    def __int__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.isMina = False
        self.adyacentes = 0

    def minasActivas(self):
        from ut03.views import generar_minas
        casilla = {(self.fila, self.columna)}
        if casilla in generar_minas:
            self.isMina = True

        return self.isMina



#clase tablero
class Tablero:
    def __init__(self, filas, columnas, nMinas):
        self.filas = CreaTableroForm.filas
        self.columnas = CreaTableroForm.columnas
        self.nMinas = CreaTableroForm.minas
        #genero la lista de coordenadas de las minas
        from ut03.views import generar_minas
        self.minas = generar_minas(filas, columnas, nMinas)
        #inicializo las casillas
        self.casillas = [[Casilla(fila, columna) for columna in range(columnas)] for fila in range(filas)]


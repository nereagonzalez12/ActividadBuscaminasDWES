from random import random

from .forms import CreaTableroForm



class Casilla:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.isMina = False
        self.adyacentes = 0

    def minasActivas(self, minas):
        casilla = (self.fila, self.columna)
        if casilla in minas:
            self.isMina = True

        return self.isMina



#clase tablero
class Tablero:
    def __init__(self, filas, columnas, nMinas):
        self.filas = filas
        self.columnas = columnas
        self.nMinas = nMinas
        #genero la lista de coordenadas de las minas
        from ut03.views import generar_minas
        self.minas = generar_minas(filas, columnas, nMinas)
        # Inicializar las casillas
        self.casillas = [[Casilla(fila, columna) for columna in range(columnas)] for fila in range(filas)]

        # Llamar al método para activar minas aquí
        self.activarMinas()

    def activarMinas(self):
        for fila in self.casillas:
            for casilla in fila:
                casilla.minasActivas(self.minas)

    def activarMinasYContarAdyacentes(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                # Activa las minas y cuenta las casillas adyacentes
                self.casillas[fila][columna].isMina = (fila, columna) in self.minas
                self.casillas[fila][columna].adyacentes = self.contarMinasAdyacentes(fila, columna)

    def contarMinasAdyacentes(self, fila, columna):
        adyacentes = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= fila + i < self.filas and 0 <= columna + j < self.columnas:
                    if self.casillas[fila + i][columna + j].isMina:
                        adyacentes += 1
        return adyacentes


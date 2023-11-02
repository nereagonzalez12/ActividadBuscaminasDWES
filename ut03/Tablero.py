from .forms import CreaTableroForm

#clase tablero
class Tablero:

    nFilas = CreaTableroForm.filas
    nColumnas = CreaTableroForm.columnas
    nMinas = CreaTableroForm.minas



    listaTablero = [[]*nColumnas]*nFilas
    #Lista de filas
    for fila in listaTablero:
        #Lista de casillas con atributos inicializados
        for col in fila:
            listaTablero[fila][col] = '-'


    coordenadasMinas = {}
    indiceFila=0
    indiceColumna=0
    for filaMinas in nMinas:
        for colMinas in filaMinas








#Clase casilla
class Casilla:
    def __int__(self, fila, columna, esMina, adyacentes):
        self.fila=fila
        self.columna=columna
        self.esMina=esMina
        self.adyacentes=adyacentes


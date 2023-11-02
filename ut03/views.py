from random import random

from django.http import Http404
from django.shortcuts import render
from .forms import CreaTableroForm
# Create your views here.
def welcome(request):
    return render(request, "ut03/index.html", {})

# La función para generar minas
def generar_minas(filas, columnas, numero_minas):
    minas = set()
    while len(minas) < numero_minas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        minas.add((fila, columna))
    return minas

def crea_tablero_form(request):
    # Si se ha enviado el formulario
    if request.method == 'POST':
        tablero_form = CreaTableroForm(request.POST)
        # Ejecutar validación
        if tablero_form.is_valid():
            # Los datos se cogen del diccionario cleaned_data
            columnas = tablero_form.cleaned_data['columnas']
            filas = tablero_form.cleaned_data['filas']
            nMinas = tablero_form.cleaned_data['minas']
            #generar minas aleatorioas
            minas = generar_minas(filas, columnas, nMinas)
            return render(request, "ut03/muestra_tablero.html",
                          {'filas': filas, 'columnas': columnas, 'minas': minas,
                           'rango_filas': range(filas), 'rango_columnas': range(columnas)})


        else:
            return render(request, "ut03/crea_tablero.html", {'form': tablero_form})
    elif request.method == "GET":
        # Si se pide la página por primera vez
        tablero_form = CreaTableroForm()
        return render(request, "ut03/crea_tablero.html", {'form': tablero_form})

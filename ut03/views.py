from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, "ut03/index.html", {})

def crea_tablero(request):
    return render(request, "ut03/crea_tablero.html", {})

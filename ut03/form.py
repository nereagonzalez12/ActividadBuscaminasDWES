from django import forms

class crea_tablero_form(forms.Form):
    filas=forms.IntegerField(label='Filas', min_value=1, max_value=20)
    columnas=forms.IntegerField(label='Colimnas', min_value=1, max_value=15)
from django import forms

class CreaTableroForm(forms.Form):
    filas=forms.IntegerField(label='Filas', min_value=1, max_value=20, required='false')
    columnas=forms.IntegerField(label='Colimnas', min_value=1, max_value=15, required='false')
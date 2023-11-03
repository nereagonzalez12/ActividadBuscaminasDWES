from mimetypes import init

from django import forms
from django.core.exceptions import ValidationError


class CreaTableroForm(forms.Form):
    filas = forms.IntegerField(label='Filas', min_value=1, max_value=20, required=False)
    columnas = forms.IntegerField(label='Columnas', min_value=1, max_value=15, required=False)
    minas = forms.IntegerField(label='Minas', min_value=1, max_value=20, required=False)
    def clean_minas(self):
        # Los datos se cogen del diccionario cleaned_data

        nMinas = self.cleaned_data['minas']
        nFilas = self.cleaned_data['filas']
        nColumnas = self.cleaned_data['columnas']


        if nMinas > (nFilas*nColumnas)//2:
            raise ValidationError("Has puesto demasiadas minas")

        return nMinas



import email
from django import forms
from .models import *
import re

#Formulario usuario
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'city',
        ]
        labels = {
            'name': 'Nombre',
            'email': 'Correo',
            'city': 'Ciudad',
        }

from django import forms
from .models import *

class FormularioJogador(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = '__all__'


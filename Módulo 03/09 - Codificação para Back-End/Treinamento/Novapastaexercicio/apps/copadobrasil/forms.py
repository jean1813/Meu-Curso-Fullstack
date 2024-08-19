from django import forms
from .models import *

class FormularioTime(forms.ModelForm):
    class Meta:
        model = Time
        fields = fields = '__all__'

class FormularioJogo(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = fields = '__all__'

from django import forms
from .models import *

class FormularioEncomenda(forms.ModelForm):
    class Meta:
        model = Encomenda
        fields = '__all__'

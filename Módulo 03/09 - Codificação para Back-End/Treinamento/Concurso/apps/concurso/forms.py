from django import forms
from .models import *


class FormularioVerconcursoUEMA(forms.ModelForm):
    class Meta:
        model = ConcursoUEMA
        fields = "__all__"


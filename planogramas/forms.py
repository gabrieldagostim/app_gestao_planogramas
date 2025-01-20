from django import forms
from .models import Planograma

class PlanogramaForm(forms.ModelForm):
    class Meta:
        model = Planograma
        fields = '__all__'  # Todos os campos do modelo
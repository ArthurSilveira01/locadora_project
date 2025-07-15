from django import forms
from .models import Automovel

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Automovel
        fields = ['placa', 'marca', 'modelo', 'ano', 'cor', 'valor_diaria', 'disponivel']
        widgets = {
            'data_cadastro' : forms.DateInput(attrs={'type' : 'date'},
                                                   format='%Y-%m-%d'),
        }
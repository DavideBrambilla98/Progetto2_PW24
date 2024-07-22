from django import forms
from .models import RicoveroTable


class RicoveroTableForm(forms.ModelForm):
    class Meta:
        model = RicoveroTable
        fields = '__all__'
        widgets = {
            'codiceRicovero' : forms.TextInput(attrs={'readonly':'readonly'}),
        }
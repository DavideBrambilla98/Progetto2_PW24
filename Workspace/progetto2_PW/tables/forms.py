import random
import string

from django import forms

from .models import RicoveroTable, PatologiaTable, CittadinoTable, OspedaleTable


class RicoveroTableForm(forms.ModelForm):

    codice = forms.ModelChoiceField(
        queryset=PatologiaTable.objects.all(),
        required=True,
        empty_label= "Seleziona patologia",
        to_field_name='codice',
        widget=forms.Select
    )
    class Meta:
        model = RicoveroTable
        fields = '__all__'
        widgets = {
            'codiceRicovero': forms.TextInput(attrs={'readonly': 'readonly'}),
            'data': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'durata': forms.NumberInput(attrs={'placeholder': 'Durata in giorni'}),
            'motivo': forms.TextInput(attrs={'placeholder': 'Motivo del ricovero'}),
            'costo': forms.NumberInput(attrs={'placeholder': 'Costo del ricovero'}),

        }


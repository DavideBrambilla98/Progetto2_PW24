import random
import string

from django import forms
from django.db.models import Max

from .models import RicoveroTable, PatologiaTable, CittadinoTable, OspedaleTable


import uuid

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

    def __init__(self, *args, **kwargs):
        super(RicoveroTableForm, self).__init__(*args, **kwargs)
        if self.instance and not self.instance.pk:  # check if it's a new instance
            unique_codiceRicovero = False
            while not unique_codiceRicovero:
                new_codiceRicovero = 'RIC-' + uuid.uuid4().hex[:8]
                if not RicoveroTable.objects.filter(codiceRicovero=new_codiceRicovero).exists():
                    unique_codiceRicovero = True
            self.initial['codiceRicovero'] = new_codiceRicovero



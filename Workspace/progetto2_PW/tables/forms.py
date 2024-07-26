from django import forms
from django.db.models import Max

from .models import RicoveroTable, PatologiaTable, CittadinoTable, OspedaleTable
import uuid # usato per generare in automatico il codice del ricovero


class RicoveroTableForm(forms.ModelForm):
    paziente = forms.ModelChoiceField(
        queryset=CittadinoTable.objects.all(),
        required=True,
        empty_label="Seleziona paziente",
        widget=forms.Select
    )
    #permette di scegliere dalla lista di tutte le patologie

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


# metodo che permette di generare in automatico il codice del rcovero controllando che non esista già nel BD
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paziente'].label_from_instance = lambda obj: f"{obj.nome} {obj.cognome}"
        super(RicoveroTableForm, self).__init__(*args, **kwargs)
        if self.instance and not self.instance.pk:  # check if it's a new instance
            unique_codiceRicovero = False
            while not unique_codiceRicovero:
                new_codiceRicovero = 'RIC-' + uuid.uuid4().hex[:12]
                if not RicoveroTable.objects.filter(codiceRicovero=new_codiceRicovero).exists():
                    unique_codiceRicovero = True
            self.initial['codiceRicovero'] = new_codiceRicovero

from django import forms

from .models import RicoveroTable, PatologiaTable, CittadinoTable, OspedaleTable


class RicoveroTableForm(forms.ModelForm):
    paziente = forms.ModelChoiceField(
        queryset=CittadinoTable.objects.all(),
        required=True,
        empty_label="Seleziona paziente",
        widget=forms.Select
    )
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
        super().__init__(*args, **kwargs)
        self.fields['paziente'].label_from_instance = lambda obj: f"{obj.nome} {obj.cognome}"

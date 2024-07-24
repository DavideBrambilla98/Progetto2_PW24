from django import forms
from .models import RicoveroTable, PatologiaTable, PersoneTable, OspedaleTable


class RicoveroTableForm(forms.ModelForm):

    paziente = forms.ModelChoiceField(
        queryset= PersoneTable.objects.all(),
        required=True,
        empty_label='Seleziona paziente',
        to_field_name='paziente',
        widget=forms.Select
    )

    codiceOspedale = forms.ModelChoiceField(
        queryset=OspedaleTable.objects.all(),
        required=True,
        empty_label='Seleziona Ospedale',
        to_field_name='codiceOspedale',
        widget=forms.Select
    )

    codPatologia = forms.ModelChoiceField(
        queryset=PatologiaTable.objects.all(),
        required=True,
        empty_label= "Seleziona patologia",
        to_field_name='codPatologia',
        widget=forms.Select
    )
    class Meta:
        model = RicoveroTable
        fields = '__all__'
        widgets = {
            'codiceRicovero' : forms.TextInput(attrs={'readonly':'readonly'}),
        }
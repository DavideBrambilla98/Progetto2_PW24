from django import forms

from .models import RicoveroTable, PatologiaTable, CittadinoTable, OspedaleTable


class RicoveroTableForm(forms.ModelForm):

    codPatologia = forms.ModelChoiceField(queryset=PatologiaTable.objects.all(), required=False)

    codFiscale = forms.ModelChoiceField(
        queryset= CittadinoTable.objects.all(),
        required=True,
        empty_label='Seleziona paziente',
        to_field_name='codFiscale',
        widget=forms.Select
    )

    codiceStruttura = forms.ModelChoiceField(
        queryset=OspedaleTable.objects.all(),
        required=True,
        empty_label='Seleziona Ospedale',
        to_field_name='codiceStruttura',
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
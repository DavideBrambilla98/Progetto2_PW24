from django import forms
from .models import RicoveroTable, PatologiaTable, CittadinoTable, OspedaleTable, PatologiaRicoveroTable
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
    codiceOspedale = forms.ModelChoiceField(
        queryset=OspedaleTable.objects.all(),
        required=True,
        empty_label="Seleziona ospedale",
        widget=forms.Select
    )


    class Meta:
        model = RicoveroTable
        fields = ['codiceRicovero', 'codiceOspedale','paziente', 'codice', 'data', 'durata', 'motivo', 'costo']

        widgets = {
            'data': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'durata': forms.NumberInput(attrs={'placeholder': 'Durata in giorni'}),
            'motivo': forms.TextInput(attrs={'placeholder': 'Motivo del ricovero'}),
            'costo': forms.NumberInput(attrs={'placeholder': 'Costo del ricovero'}),
        }


# metodo che permette di generare in automatico il codice del rcovero controllando che non esista già nel BD
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paziente'].label_from_instance = lambda obj: f"{obj.nome} {obj.cognome}"

        if self.instance and self.instance.pk:
            try:
                # Trova il record corrispondente nel modello PatologiaRicoveroTable
                patologia_ricovero = PatologiaRicoveroTable.objects.filter(
                    codRicovero=self.instance,
                    codOspedale=self.instance.codiceOspedale
                ).first()

                if patologia_ricovero:
                    self.fields['codice'].initial = patologia_ricovero.codPatologia
                    self.fields['codiceOspedale'].initial = patologia_ricovero.codOspedale

            except PatologiaRicoveroTable.DoesNotExist:
                pass

        else:
            if self.instance and not self.instance.pk:
                unique_codiceRicovero = False
                while not unique_codiceRicovero:
                    new_codiceRicovero = 'RIC-' + uuid.uuid4().hex[:12]
                    if not RicoveroTable.objects.filter(codiceRicovero=new_codiceRicovero).exists():
                        unique_codiceRicovero = True
                self.initial['codiceRicovero'] = new_codiceRicovero

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        codPatologia = self.cleaned_data.get('codice')
        codOspedale = self.cleaned_data.get('codiceOspedale')

        if codPatologia and codOspedale:
            PatologiaRicoveroTable.objects.update_or_create(
                codRicovero=instance,
                codOspedale=codOspedale,
                defaults={
                    'codPatologia': codPatologia,
                }
            )
        return instance
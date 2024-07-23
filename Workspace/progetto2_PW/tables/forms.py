from django import forms
from .models import RicoveroTable, PatologiaTable


class RicoveroTableForm(forms.ModelForm):

    codPatologia = forms.ModelChoiceField(queryset=PatologiaTable.objects.all(), required=False)
    class Meta:
        model = RicoveroTable
        fields = '__all__'
        widgets = {
            'codiceRicovero' : forms.TextInput(attrs={'readonly':'readonly'}),
        }
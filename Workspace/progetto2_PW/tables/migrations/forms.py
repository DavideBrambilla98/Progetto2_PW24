from django import forms
from .models import RicoveroTable


class RicoveroTableForm(forms.ModelForm):
    class Meta:
        model = RicoveroTable
        fields = '__all__'
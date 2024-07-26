from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, F, Value
from django.db.models.functions import Concat
from .models import PatologiaTable, RicoveroTable, OspedaleTable, CittadinoTable, PatologiaRicoveroTable
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tables.forms import RicoveroTableForm

def searchPatologie(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')
    if search_option == '3' or search_option == '4' or search_option == '5' or search_option == '6':
        search_value = '1'

    if search_option and search_value:
        if search_option == '1':
            queryset = PatologiaTable.objects.filter(nome__icontains=search_value)
        elif search_option == '2':
            queryset = PatologiaTable.objects.filter(criticita__icontains=search_value)
        elif search_option == '3':
            queryset = PatologiaTable.objects.filter(Q(cronica='1') & ~Q(mortale='1'))
        elif search_option == '4':
            queryset = PatologiaTable.objects.filter(~Q(cronica='1') & Q(mortale='1'))
        elif search_option == '5':
            queryset = PatologiaTable.objects.filter(Q(cronica='1') & Q(mortale='1'))
        elif search_option == '6':
            queryset = PatologiaTable.objects.filter(~Q(cronica='1') & ~Q(mortale='1'))
    else:
        queryset = PatologiaTable.objects.all()

    return render(request, 'Patologie.html', {'queryset': queryset})

def searchOspedali(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    if search_option and search_value:
        if search_option == '1':
            queryset = OspedaleTable.objects.filter(denominazioneStruttura__icontains=search_value)
        elif search_option == '2':
            queryset = OspedaleTable.objects.filter(comune__icontains=search_value)
        elif search_option == '3':
            queryset = OspedaleTable.objects.filter(direttoreSanitario__icontains=search_value)
    else:
        queryset = OspedaleTable.objects.all()

    return render(request, 'Ospedali.html', {'queryset': queryset})

def searchRicoveri(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    if search_option and search_value:
        if search_option == '1':
            # Annotate con il campo concatenato
            queryset = RicoveroTable.objects.annotate(
                paziente_full_name=Concat(
                    'paziente__nome',
                    Value(' '),  # Aggiungi uno spazio tra nome e cognome
                    'paziente__cognome'
                )
            ).filter(
                paziente_full_name__icontains=search_value
            )
        elif search_option == '2':
            queryset = RicoveroTable.objects.filter(paziente__codFiscale__icontains=search_value)
        elif search_option == '3':
            queryset = RicoveroTable.objects.filter(codiceOspedale__denominazioneStruttura__icontains=search_value)
    else:
        queryset = RicoveroTable.objects.select_related('paziente','codiceOspedale').all() #paziente è il nome del campo foreignkey diRicoveroTable

    return render(request, 'Ricoveri.html', {'queryset': queryset})

def searchCittadini(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    if search_option and search_value:
        if search_option == '1':
            queryset = CittadinoTable.objects.filter(cognome__icontains=search_value)
        elif search_option == '2':
            queryset = CittadinoTable.objects.filter(codFiscale__icontains=search_value)
        elif search_option == '3':
            queryset = CittadinoTable.objects.filter(dataNascita__icontains=search_value)
        elif search_option == '4':
            queryset = CittadinoTable.objects.filter(nasLuogo__icontains=search_value)
        elif search_option == '5':
            queryset = CittadinoTable.objects.filter(indirizzo__icontains=search_value)
    else:
        queryset = CittadinoTable.objects.all()

    return render(request, 'Cittadini.html', {'queryset': queryset})
class RicoveroTableCreate(CreateView):
    model = RicoveroTable
    form_class = RicoveroTableForm
    template_name = 'crud.html'
    success_url = reverse_lazy('listaRic')

    def form_valid(self, form):
        response = super().form_valid(form)
        codPatologia = form.cleaned_data.get('codPatologia')
        if codPatologia:
            PatologiaRicoveroTable.objects.create(
                codRicovero = self.object,
                codPatologia = codPatologia,
                codOspedale = self.object
            )
        return response

class RicoveroTableUpdate(UpdateView):
    model = RicoveroTable
    form_class = RicoveroTableForm
    template_name = 'crud.html'
    success_url = reverse_lazy('listaRic')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        if 'codiceRicovero' in form.fields:
            form.fields['codiceRicovero'].widget.attrs['readonly'] = True
        return form
    def form_valid(self, form):
        response = super().form_valid(form)
        codPatologia = form.cleaned_data.get('codPatologia')

        if codPatologia:
            records = RicoveroTable.objects.filter(codiceRicovero=self.object)
            for record in records:
                record.codPatologia = codPatologia
                record.codOspedale = self.object.codOspedale
                record.save()
        return response

class RicoveroTableDelete(DeleteView):
    model = RicoveroTable
    template_name = 'crud_delete.html'
    success_url = reverse_lazy('listaRic')
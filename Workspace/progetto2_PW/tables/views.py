
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, F, Value, Count
from django.db.models.functions import Concat
from .models import PatologiaTable, RicoveroTable, OspedaleTable, CittadinoTable, PatologiaRicoveroTable
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tables.forms import RicoveroTableForm

def searchPatologie(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    queryset = PatologiaTable.objects.all().order_by('nome')
    patologie_con_ricoveri = queryset.annotate(
        numero_ricoveri=Count('patologiaricoverotable')
    ).order_by('nome')

    if search_option == '3' or search_option == '4' or search_option == '5' or search_option == '6':
        search_value = '1'

    if search_option and search_value:
        if search_option == '1':
            patologie_con_ricoveri = patologie_con_ricoveri.filter(nome__icontains=search_value)
        elif search_option == '2':
            patologie_con_ricoveri = patologie_con_ricoveri.filter(criticita__icontains=search_value)
        elif search_option == '3':
            patologie_con_ricoveri = patologie_con_ricoveri.filter(Q(cronica='1') & ~Q(mortale='1'))
        elif search_option == '4':
            patologie_con_ricoveri = patologie_con_ricoveri.filter(~Q(cronica='1') & Q(mortale='1'))
        elif search_option == '5':
            patologie_con_ricoveri = patologie_con_ricoveri.filter(Q(cronica='1') & Q(mortale='1'))
        elif search_option == '6':
            patologie_con_ricoveri = patologie_con_ricoveri.filter(~Q(cronica='1') & ~Q(mortale='1'))
        elif search_option == '7':
            patologie_con_ricoveri = patologie_con_ricoveri.filter(
                patologiaricoverotable__codRicovero__codiceRicovero=search_value)

    return render(request, 'Patologie.html', {'queryset': patologie_con_ricoveri})


def searchOspedali(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    queryset = OspedaleTable.objects.all().order_by('denominazioneStruttura')
    ospedali_con_ricoveri = queryset.annotate(
        numero_ricoveri=Count('ricoverotable')
    ).order_by('denominazioneStruttura')

    if search_option and search_value:
        if search_option == '1':
            ospedali_con_ricoveri = ospedali_con_ricoveri.filter(denominazioneStruttura__icontains=search_value)
        elif search_option == '2':
            ospedali_con_ricoveri = ospedali_con_ricoveri.filter(comune__icontains=search_value)
        elif search_option == '3':
            ospedali_con_ricoveri = ospedali_con_ricoveri.annotate(
                paziente_full_name=Concat(
                    'direttoreSanitario__nome',
                    Value(' '),  # Add a space between first name and last name
                    'direttoreSanitario__cognome'
                )
            ).filter(
                paziente_full_name__icontains=search_value
            )
        elif search_option == '4':
            ospedali_con_ricoveri = ospedali_con_ricoveri.filter(codiceStruttura__icontains=search_value)

    return render(request, 'Ospedali.html', {'queryset': ospedali_con_ricoveri})


def searchRicoveri(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    queryset = RicoveroTable.objects.select_related('paziente','codiceOspedale').all().order_by('paziente__nome')
    ricoveri_con_patologie = queryset.annotate(
        numero_patologie=Count('patologiaricoverotable')
    ).order_by('paziente__nome')

    if search_option and search_value:
        if search_option == '1':
            ricoveri_con_patologie = ricoveri_con_patologie.annotate(
                paziente_full_name=Concat(
                    'paziente__nome',
                    Value(' '),  # Add a space between first name and last name
                    'paziente__cognome'
                )
            ).filter(
                paziente_full_name__icontains=search_value
            )
        elif search_option == '2':
            ricoveri_con_patologie = ricoveri_con_patologie.filter(paziente__codFiscale__icontains=search_value)
        elif search_option == '3':
            ricoveri_con_patologie = ricoveri_con_patologie.filter(codiceOspedale__denominazioneStruttura__icontains=search_value)
        elif search_option == '4':
            ricoveri_con_patologie = ricoveri_con_patologie.filter(patologiaricoverotable__codPatologia__codice=search_value)

    return render(request, 'Ricoveri.html', {'queryset': ricoveri_con_patologie})


def searchCittadini(request):
    search_option = request.GET.get('inlineFormCustomSelect', '')
    search_value = request.GET.get('cerca', '')

    # Esegui il conteggio prima di applicare il filtro
    queryset = CittadinoTable.objects.all().order_by('nome')
    cittadini_con_ricoveri = queryset.annotate(
        numero_ricoveri=Count('ricoverotable')
    ).order_by('nome')

    if search_option and search_value:
        if search_option == '1':
            cittadini_con_ricoveri = cittadini_con_ricoveri.annotate(
                paziente_full_name=Concat(
                    'nome',
                    Value(' '),  # Add a space between first name and last name
                    'cognome'
                )
            ).filter(
                paziente_full_name__icontains=search_value
            )
        elif search_option == '2':
            cittadini_con_ricoveri = cittadini_con_ricoveri.filter(codFiscale__icontains=search_value)
        elif search_option == '3':
            cittadini_con_ricoveri = cittadini_con_ricoveri.filter(dataNascita__icontains=search_value)
        elif search_option == '4':
            cittadini_con_ricoveri = cittadini_con_ricoveri.filter(nasLuogo__icontains=search_value)
        elif search_option == '5':
            cittadini_con_ricoveri = cittadini_con_ricoveri.filter(indirizzo__icontains=search_value)

    return render(request, 'Cittadini.html', {'queryset': cittadini_con_ricoveri})


class RicoveroTableCreate(CreateView):
    model = RicoveroTable
    form_class = RicoveroTableForm
    template_name = 'crud.html'
    success_url = reverse_lazy('listaRic')

class RicoveroTableUpdate(UpdateView):
    model = RicoveroTable
    form_class = RicoveroTableForm
    template_name = 'crud.html'
    success_url = reverse_lazy('listaRic')

class RicoveroTableDelete(DeleteView):
    model = RicoveroTable
    template_name = 'crud_delete.html'
    success_url = reverse_lazy('listaRic')


def disclaimer(request):
    return render(request, 'disclaimer.html')

